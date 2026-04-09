from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Sequence
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


CONTEXT_FILES = {
    "brand_voice": "context/brand-voice.md",
    "style_guide": "context/style-guide.md",
    "seo_guidelines": "context/seo-guidelines.md",
    "features": "context/features.md",
    "internal_links": "context/internal-links-map.md",
    "target_keywords": "context/target-keywords.md",
    "writing_examples": "context/writing-examples.md",
    "competitor_analysis": "context/competitor-analysis.md",
}

TEMPLATE_MARKERS = (
    "[YOUR COMPANY]",
    "[yoursite.com]",
    "[VOICE PILLAR NAME]",
    "[Product/Service Name",
    "[Feature Name",
    "[Resource Name",
    "[MESSAGE TITLE]",
    "[DESCRIBE",
    "<!-- INSTRUCTIONS:",
)

DEFAULT_TARGET_WORD_COUNT = "2200-2800"


@dataclass
class ContextStatus:
    key: str
    path: Path
    ready: bool
    notes: List[str]


@dataclass
class ArticleMetadata:
    title: str
    meta_title: str
    meta_description: str
    primary_keyword: str
    secondary_keywords: List[str]
    slug: str


class MissingDependencyError(RuntimeError):
    """Raised when an optional runtime dependency is missing."""


def repo_path(relative_path: str) -> Path:
    return REPO_ROOT / relative_path


def today_iso() -> str:
    return date.today().isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug) or "untitled"


def title_case(value: str) -> str:
    words = re.sub(r"[-_]+", " ", value).split()
    return " ".join(word.capitalize() for word in words)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write_text(path: Path, content: str, overwrite: bool = False) -> Path:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Use --overwrite to replace it.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def detect_context_status(key: str, path: Path) -> ContextStatus:
    content = read_text(path)
    notes: List[str] = []

    if not content.strip():
        notes.append("missing or empty")
        return ContextStatus(key=key, path=path, ready=False, notes=notes)

    for marker in TEMPLATE_MARKERS:
        if marker in content:
            notes.append(f"template marker present: {marker}")

    if len(content.strip()) < 400:
        notes.append("file is unusually short")

    ready = not notes
    return ContextStatus(key=key, path=path, ready=ready, notes=notes or ["ready"])


def audit_context() -> List[ContextStatus]:
    return [
        detect_context_status(key, repo_path(relative_path))
        for key, relative_path in CONTEXT_FILES.items()
    ]


def format_context_audit(statuses: Sequence[ContextStatus]) -> str:
    ready_count = sum(1 for status in statuses if status.ready)
    lines = [
        "# Context Audit",
        "",
        f"**Date**: {today_iso()}",
        f"**Ready Files**: {ready_count}/{len(statuses)}",
        "",
    ]

    for status in statuses:
        state = "ready" if status.ready else "needs work"
        lines.append(f"## {status.key}")
        lines.append(f"- **Path**: {status.path.relative_to(REPO_ROOT)}")
        lines.append(f"- **Status**: {state}")
        for note in status.notes:
            lines.append(f"- **Note**: {note}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def extract_field(text: str, *field_names: str) -> str:
    patterns = []
    for field_name in field_names:
        escaped = re.escape(field_name)
        patterns.extend(
            [
                rf"^\*\*{escaped}\*\*:\s*(.+?)\s*$",
                rf"^- \*\*{escaped}\*\*:\s*(.+?)\s*$",
                rf"^{escaped}:\s*(.+?)\s*$",
            ]
        )

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
    return ""


def split_csv(value: str) -> List[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def section_text(text: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        return ""

    start = match.end()
    remainder = text[start:]
    next_heading = re.search(r"^##\s+.+$", remainder, re.MULTILINE)
    end = next_heading.start() if next_heading else len(remainder)
    return remainder[:end].strip()


def parse_section_bullets(text: str, heading: str) -> List[str]:
    body = section_text(text, heading)
    items = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            value = stripped[2:].strip()
            if value and "TBD" not in value:
                items.append(value)
    return items


def parse_brief(text: str) -> Dict[str, object]:
    return {
        "primary_keyword": extract_field(text, "Primary Keyword", "Target Keyword"),
        "secondary_keywords": split_csv(extract_field(text, "Secondary Keywords")),
        "meta_title": extract_field(text, "Meta Title"),
        "meta_description": extract_field(text, "Meta Description"),
        "outline": parse_section_bullets(text, "Recommended Outline"),
        "gaps": parse_section_bullets(text, "Content Gaps & Opportunities"),
        "insights": parse_section_bullets(text, "Unique Insights to Use"),
        "internal_links": parse_section_bullets(text, "Internal Link Candidates"),
    }


def extract_urls(text: str) -> List[str]:
    return re.findall(r"https?://[^\s)\]]+", text)


def internal_domains() -> List[str]:
    links_map = read_text(repo_path(CONTEXT_FILES["internal_links"]))
    domains = []
    for url in extract_urls(links_map):
        try:
            parsed = urlparse(url)
        except ValueError:
            continue
        if parsed.netloc and "[" not in parsed.netloc:
            domains.append(parsed.netloc.lower())
    return sorted(set(domains))


def collect_internal_link_candidates(limit: int = 8) -> List[str]:
    links_map = read_text(repo_path(CONTEXT_FILES["internal_links"]))
    candidates = []
    current_heading = ""

    for line in links_map.splitlines():
        stripped = line.strip()
        heading_match = re.match(r"^###\s+(.+)$", stripped)
        if heading_match:
            current_heading = heading_match.group(1).strip()
            continue

        url_match = re.match(r"^- \*\*URL\*\*:\s*(https?://\S+)", stripped, re.IGNORECASE)
        if url_match and current_heading:
            url = url_match.group(1).strip()
            if "[" not in url:
                candidates.append(f"{current_heading} - {url}")

    return candidates[:limit]


def default_brief_path(topic: str) -> Path:
    return repo_path(f"research/brief-{slugify(topic)}-{today_iso()}.md")


def default_plan_path(topic: str) -> Path:
    return repo_path(f"research/article-plan-{slugify(topic)}-{today_iso()}.md")


def default_optimize_report_path(article_path: Path) -> Path:
    return article_path.with_name(f"optimization-{article_path.stem}-{today_iso()}.md")


def default_quartz_export_path(content_root: Path, folder: str, topic_or_slug: str) -> Path:
    normalized_folder = folder.strip("/\\")
    if normalized_folder:
        return content_root / normalized_folder / f"{slugify(topic_or_slug)}.md"
    return content_root / f"{slugify(topic_or_slug)}.md"


def default_quartz_project_dir() -> Path:
    return repo_path("site/quartz-site")


def build_quartz_build_args(
    content_dir: Path,
    output_dir: str = "public",
    serve: bool = False,
    watch: bool = False,
    port: Optional[int] = None,
    ws_port: Optional[int] = None,
) -> List[str]:
    args = [
        "npx",
        "quartz",
        "build",
        "-d",
        str(content_dir),
        "-o",
        output_dir,
    ]
    if serve:
        args.append("--serve")
    if watch:
        args.append("--watch")
    if port is not None:
        args.extend(["--port", str(port)])
    if ws_port is not None:
        args.extend(["--wsPort", str(ws_port)])
    return args


def resolve_node_executable(name: str) -> str:
    if os.name == "nt":
        return f"{name}.cmd"
    return name


def yaml_escape(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def extract_date_from_path(path: Path) -> str:
    match = re.search(r"(\d{4}-\d{2}-\d{2})", path.stem)
    return match.group(1) if match else today_iso()


def strip_article_metadata(article_content: str, title: str) -> str:
    body = article_content
    h1_pattern = rf"^#\s+{re.escape(title)}\s*$"
    body = re.sub(h1_pattern, "", body, count=1, flags=re.IGNORECASE | re.MULTILINE)

    metadata_patterns = [
        r"^\*\*Meta Title\*\*:\s*.+$",
        r"^\*\*Meta Description\*\*:\s*.+$",
        r"^\*\*Primary Keyword\*\*:\s*.+$",
        r"^\*\*Target Keyword\*\*:\s*.+$",
        r"^\*\*Secondary Keywords\*\*:\s*.+$",
        r"^\*\*URL Slug\*\*:\s*.+$",
        r"^\*\*Internal Links\*\*:\s*.+$",
        r"^\*\*External Links\*\*:\s*.+$",
        r"^\*\*Word Count\*\*:\s*.+$",
        r"^\*\*Category\*\*:\s*.+$",
        r"^\*\*Tags\*\*:\s*.+$",
    ]

    for pattern in metadata_patterns:
        body = re.sub(pattern, "", body, flags=re.IGNORECASE | re.MULTILINE)

    body = re.sub(r"^\s*---\s*$", "", body, count=1, flags=re.MULTILINE)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"


def is_internal_target(target: str, internal_domains_list: Sequence[str]) -> bool:
    if target.startswith("/"):
        return True
    if target.endswith(".md"):
        return True

    parsed = urlparse(target)
    if parsed.scheme not in {"http", "https"}:
        return False

    domain = parsed.netloc.lower()
    return any(domain == known or domain.endswith(f".{known}") for known in internal_domains_list)


def normalize_note_reference(target: str) -> Optional[str]:
    parsed = urlparse(target)
    parsed_path = parsed.path or target.split("#", 1)[0]
    parsed_fragment = parsed.fragment

    if not parsed_path:
        return None

    cleaned = parsed_path.strip("/").replace("\\", "/")
    if cleaned.endswith(".md"):
        cleaned = cleaned[:-3]

    if not cleaned:
        return None

    basename = cleaned.split("/")[-1]
    basename = basename.strip()
    if not basename:
        return None

    fragment = parsed_fragment or ""
    if "#" in basename:
        base, suffix = basename.split("#", 1)
        return f"{base}#{suffix}"
    if fragment:
        return f"{basename}#{fragment}"
    return basename


def convert_internal_markdown_links_to_wikilinks(
    content: str,
    internal_domains_list: Sequence[str],
) -> str:
    pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")

    def replacer(match: re.Match[str]) -> str:
        label = match.group(1).strip()
        target = match.group(2).strip()
        if not is_internal_target(target, internal_domains_list):
            return match.group(0)

        note_ref = normalize_note_reference(target)
        if not note_ref:
            return match.group(0)

        return f"[[{note_ref}|{label}]]"

    return pattern.sub(replacer, content)


def build_quartz_note_markdown(
    article_content: str,
    source_path: Path,
    internal_domains_list: Sequence[str],
    publish: bool,
    tags: Sequence[str],
) -> str:
    metadata = article_metadata(article_content, source_path)
    body = strip_article_metadata(article_content, metadata.title)
    body = convert_internal_markdown_links_to_wikilinks(body, internal_domains_list)

    normalized_tags = [tag.strip() for tag in tags if tag.strip()]
    note_date = extract_date_from_path(source_path)

    lines = [
        "---",
        f"title: {yaml_escape(metadata.title)}",
    ]

    if metadata.meta_description:
        lines.append(f"description: {yaml_escape(metadata.meta_description)}")

    lines.extend(
        [
            f"date: {note_date}",
            f"modified: {today_iso()}",
            f"draft: {'false' if publish else 'true'}",
            f"publish: {'true' if publish else 'false'}",
        ]
    )

    if normalized_tags:
        lines.append("tags:")
        for tag in normalized_tags:
            lines.append(f"  - {tag}")

    alias = metadata.meta_title.strip()
    if alias and alias != metadata.title:
        lines.append("aliases:")
        lines.append(f"  - {yaml_escape(alias)}")

    lines.extend(["---", "", body.strip(), ""])
    return "\n".join(lines)


def build_brief_markdown(topic: str, statuses: Sequence[ContextStatus]) -> str:
    from data_sources.modules.article_planner import create_default_structure

    slug = slugify(topic)
    links = collect_internal_link_candidates()
    ready_files = [status.key for status in statuses if status.ready]
    blocked_files = [status.key for status in statuses if not status.ready]

    lines = [
        f"# Research Brief: {topic}",
        "",
        f"**Date**: {today_iso()}",
        f"**Topic**: {topic}",
        f"**Status**: scaffold - replace each TBD with verified research",
        "",
        "## Context Readiness",
        f"- Ready context files: {', '.join(ready_files) if ready_files else 'none yet'}",
        f"- Files that still need customization: {', '.join(blocked_files) if blocked_files else 'none'}",
        "",
        "## SEO Foundation",
        "- **Primary Keyword**: TBD",
        "- **Search Intent**: TBD",
        "- **Secondary Keywords**: TBD, TBD, TBD",
        f"- **Target Word Count**: {DEFAULT_TARGET_WORD_COUNT}",
        "- **Featured Snippet Opportunity**: TBD",
        "",
        "## Competitive Landscape",
        "- Top competitor article 1: TBD",
        "- Top competitor article 2: TBD",
        "- Top competitor article 3: TBD",
        "- Must-cover themes from SERP: TBD",
        "",
        "## Content Gaps & Opportunities",
        "- Gap 1: TBD",
        "- Gap 2: TBD",
        "- Gap 3: TBD",
        "",
        "## Unique Insights to Use",
        "- Insight 1: tie the topic to your product or service advantage",
        "- Insight 2: add a concrete scenario with numbers and outcomes",
        "- Insight 3: include a contrarian or under-covered angle",
        "",
        "## Recommended Outline",
    ]

    for heading in create_default_structure(topic):
        lines.append(f"- {heading}")

    lines.extend(["", "## Internal Link Candidates"])
    if links:
        for item in links:
            lines.append(f"- {item}")
    else:
        lines.append("- Add your key internal URLs to context/internal-links-map.md")

    lines.extend(
        [
            "",
            "## Meta Elements Preview",
            f"- **Meta Title**: {title_case(topic)}: Complete Guide",
            f"- **Meta Description**: Learn {topic} with practical examples, clear steps, and next actions.",
            f"- **URL Slug**: /blog/{slug}",
            "",
            "## Research Checklist",
            "- Verify search intent with live SERP review.",
            "- Collect 3-5 trustworthy sources for statistics and claims.",
            "- Note what competitors cover well and where they stay thin.",
            "- Replace every TBD before drafting.",
            "",
            "## Codex Notes",
            f"- Draft target path: drafts/{slug}-{today_iso()}.md",
            f"- Planning command: python scripts/codex_seo_machine.py plan \"{topic}\" --brief research/brief-{slug}-{today_iso()}.md",
            "- Optimization command: python scripts/codex_seo_machine.py optimize <draft-path>",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def build_article_metadata(topic: str, brief_data: Dict[str, object]) -> ArticleMetadata:
    primary_keyword = str(brief_data.get("primary_keyword") or topic).strip()
    secondary_keywords = [
        keyword for keyword in brief_data.get("secondary_keywords", []) if isinstance(keyword, str)
    ]
    slug = slugify(primary_keyword or topic)
    meta_title = str(brief_data.get("meta_title") or f"{title_case(topic)}: Complete Guide")
    meta_description = str(
        brief_data.get("meta_description")
        or f"Learn {topic} with practical steps, examples, and SEO-ready recommendations."
    )

    return ArticleMetadata(
        title=title_case(topic),
        meta_title=meta_title,
        meta_description=meta_description,
        primary_keyword=primary_keyword,
        secondary_keywords=secondary_keywords,
        slug=slug,
    )


def _cycle_assignments(items: List[str], section_count: int) -> Dict[int, List[str]]:
    assignments: Dict[int, List[str]] = {index: [] for index in range(1, section_count + 1)}
    if not items:
        return assignments

    section_indices = list(range(2, max(2, section_count))) or [1]
    for offset, item in enumerate(items):
        section_number = section_indices[offset % len(section_indices)]
        assignments[section_number].append(item)
    return assignments


def build_plan_markdown(topic: str, brief_text: str) -> str:
    from data_sources.modules.article_planner import (
        ArticlePlan,
        ArticlePlanner,
        MetaElements,
        create_default_structure,
        format_article_plan,
    )
    from data_sources.modules.section_writer import (
        SectionType as WriterSectionType,
        format_editing_prompt,
        format_writing_prompt,
    )

    brief_data = parse_brief(brief_text)
    metadata = build_article_metadata(topic, brief_data)
    outline = brief_data["outline"] or create_default_structure(topic)
    internal_links = brief_data["internal_links"] or collect_internal_link_candidates(limit=6)
    gaps = brief_data["gaps"]
    insights = brief_data["insights"]

    planner = ArticlePlanner()
    engagement_map = planner.plan_engagement_distribution(len(outline))
    gap_assignments = _cycle_assignments(gaps, len(outline))
    insight_assignments = _cycle_assignments(insights, len(outline))

    sections = []
    gap_mapping: Dict[str, int] = {}
    insight_mapping: Dict[str, int] = {}
    for index, heading in enumerate(outline, start=1):
        section_gaps = gap_assignments.get(index, [])
        section_insights = insight_assignments.get(index, [])
        section_links = internal_links[:3]

        for gap in section_gaps:
            gap_mapping[gap] = index
        for insight in section_insights:
            insight_mapping[insight] = index

        sections.append(
            planner.create_section_plan(
                section_number=index,
                heading=heading,
                gaps_to_address=section_gaps,
                insights_to_include=section_insights,
                internal_links=section_links,
                engagement_map=engagement_map,
            )
        )

    meta = MetaElements(
        title_options=[
            metadata.meta_title,
            f"How to {title_case(topic)}",
            f"{title_case(topic)} Best Practices",
        ],
        meta_title=metadata.meta_title,
        meta_description=metadata.meta_description,
        url_slug=metadata.slug,
        primary_keyword=metadata.primary_keyword,
        secondary_keywords=metadata.secondary_keywords,
    )

    plan = ArticlePlan(
        topic=topic,
        date=today_iso(),
        meta=meta,
        total_word_target=sum(section.word_target for section in sections),
        sections=sections,
        engagement_map=engagement_map,
        gap_to_section_mapping=gap_mapping,
        insight_to_section_mapping=insight_mapping,
    )

    markdown = format_article_plan(plan)
    markdown += "\n---\n\n## Section Writing Prompts\n\n"

    for section in sections:
        writer_section_type = WriterSectionType(section.section_type.value)
        cta_value = section.cta_type.value if section.cta_type else ""

        markdown += f"### Prompt for Section {section.section_number}: {section.heading}\n\n"
        markdown += "```text\n"
        markdown += format_writing_prompt(
            section_type=writer_section_type,
            heading=section.heading,
            word_target=section.word_target,
            strategic_angle=section.strategic_angle,
            unique_data=section.unique_data_to_include,
            internal_links=section.internal_links,
            has_mini_story=section.mini_story_planned,
            has_cta=cta_value,
        ).strip()
        markdown += "\n```\n\n"

        markdown += "```text\n"
        markdown += format_editing_prompt(
            section_type=writer_section_type,
            draft="[Paste the drafted section here before editing.]",
        ).strip()
        markdown += "\n```\n\n"

    markdown += (
        "## Draft Assembly Notes\n\n"
        f"- Draft file name: `drafts/{metadata.slug}-{today_iso()}.md`\n"
        "- Keep metadata fields at the top of the markdown file.\n"
        "- After the draft is complete, run the optimize command.\n"
    )

    return markdown


def load_article(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Article not found: {path}")
    return path.read_text(encoding="utf-8")


def article_metadata(content: str, file_path: Path) -> ArticleMetadata:
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = h1_match.group(1).strip() if h1_match else title_case(file_path.stem)
    primary_keyword = extract_field(content, "Primary Keyword", "Target Keyword") or title
    secondary_keywords = split_csv(extract_field(content, "Secondary Keywords"))
    slug = extract_field(content, "URL Slug")
    slug = slug.replace("/blog/", "").strip("/") if slug else slugify(primary_keyword)
    meta_title = extract_field(content, "Meta Title") or title
    meta_description = extract_field(content, "Meta Description")
    return ArticleMetadata(
        title=title,
        meta_title=meta_title,
        meta_description=meta_description,
        primary_keyword=primary_keyword,
        secondary_keywords=secondary_keywords,
        slug=slug,
    )


def count_links(content: str) -> Dict[str, int]:
    markdown_links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)
    domains = internal_domains()
    internal = 0
    external = 0

    for link in markdown_links:
        if link.startswith("/"):
            internal += 1
            continue
        if link.startswith("http://") or link.startswith("https://"):
            domain = urlparse(link).netloc.lower()
            if any(domain == known or domain.endswith(f".{known}") for known in domains):
                internal += 1
            else:
                external += 1

    return {"internal": internal, "external": external}


def import_optional_components():
    try:
        from data_sources.modules.readability_scorer import ReadabilityScorer
        from data_sources.modules.seo_quality_rater import SEOQualityRater
        from data_sources.modules.keyword_analyzer import KeywordAnalyzer
        from data_sources.modules.search_intent_analyzer import SearchIntentAnalyzer
        from data_sources.modules.content_scrubber import ContentScrubber
        from data_sources.modules.content_scorer import ContentScorer
    except ModuleNotFoundError as exc:
        if exc.name and not exc.name.startswith("data_sources"):
            raise MissingDependencyError(
                f"Missing dependency '{exc.name}'. Install requirements with "
                "`pip install -r data_sources/requirements.txt`."
            ) from exc
        raise

    return {
        "ContentScrubber": ContentScrubber,
        "ContentScorer": ContentScorer,
        "KeywordAnalyzer": KeywordAnalyzer,
        "ReadabilityScorer": ReadabilityScorer,
        "SearchIntentAnalyzer": SearchIntentAnalyzer,
        "SEOQualityRater": SEOQualityRater,
    }


def build_optimization_report(article_path: Path, content: str, scrub_stats: Dict[str, int]) -> str:
    components = import_optional_components()
    metadata = article_metadata(content, article_path)
    links = count_links(content)

    keyword_result = components["KeywordAnalyzer"]().analyze(
        content=content,
        primary_keyword=metadata.primary_keyword,
        secondary_keywords=metadata.secondary_keywords,
    )
    readability_result = components["ReadabilityScorer"]().analyze(content)
    seo_result = components["SEOQualityRater"]().rate(
        content=content,
        meta_title=metadata.meta_title,
        meta_description=metadata.meta_description,
        primary_keyword=metadata.primary_keyword,
        secondary_keywords=metadata.secondary_keywords,
        keyword_density=keyword_result["primary_keyword"]["density"],
        internal_link_count=links["internal"],
        external_link_count=links["external"],
    )
    content_score = components["ContentScorer"]().score(
        content=content,
        metadata={
            "meta_title": metadata.meta_title,
            "meta_description": metadata.meta_description,
            "primary_keyword": metadata.primary_keyword,
            "secondary_keywords": metadata.secondary_keywords,
        },
    )
    intent_result = components["SearchIntentAnalyzer"]().analyze(metadata.primary_keyword)

    lines = [
        f"# Optimization Report: {article_path.name}",
        "",
        f"**Date**: {today_iso()}",
        f"**Draft**: {article_path}",
        f"**Primary Keyword**: {metadata.primary_keyword}",
        "",
        "## Summary",
        f"- Composite content score: {content_score['composite_score']}/100",
        f"- SEO quality score: {seo_result['overall_score']}/100",
        f"- Readability score: {readability_result.get('overall_score', 'n/a')}/100",
        f"- Search intent: {intent_result['primary_intent']}",
        f"- Publishing ready: {'yes' if seo_result['publishing_ready'] else 'no'}",
        "",
        "## Scrubbing",
        f"- Unicode watermarks removed: {scrub_stats.get('unicode_removed', 0)}",
        f"- Format-control characters removed: {scrub_stats.get('format_control_removed', 0)}",
        f"- Em-dashes replaced: {scrub_stats.get('emdashes_replaced', 0)}",
        "",
        "## Keyword Analysis",
        f"- Density: {keyword_result['primary_keyword']['density']}%",
        f"- Exact matches: {keyword_result['primary_keyword']['exact_matches']}",
        f"- Total occurrences: {keyword_result['primary_keyword']['total_occurrences']}",
        f"- Status: {keyword_result['primary_keyword']['density_status']}",
        "",
        "## Link Counts",
        f"- Internal links: {links['internal']}",
        f"- External links: {links['external']}",
        "",
        "## Readability",
        f"- Grade: {readability_result.get('grade', 'n/a')}",
        f"- Flesch reading ease: {readability_result.get('readability_metrics', {}).get('flesch_reading_ease', 'n/a')}",
        f"- Flesch-Kincaid grade: {readability_result.get('readability_metrics', {}).get('flesch_kincaid_grade', 'n/a')}",
        f"- Average sentence length: {readability_result.get('structure_analysis', {}).get('avg_sentence_length', 'n/a')}",
        "",
        "## SEO Issues",
    ]

    critical_issues = seo_result.get("critical_issues", [])
    warnings = seo_result.get("warnings", [])
    suggestions = seo_result.get("suggestions", [])
    if critical_issues:
        for issue in critical_issues:
            lines.append(f"- Critical: {issue}")
    else:
        lines.append("- Critical: none")
    for warning in warnings[:5]:
        lines.append(f"- Warning: {warning}")
    for suggestion in suggestions[:5]:
        lines.append(f"- Suggestion: {suggestion}")

    lines.extend(["", "## Priority Fixes"])
    priority_fixes = content_score.get("priority_fixes", [])
    if priority_fixes:
        for fix in priority_fixes:
            lines.append(f"- {fix.get('message', fix)}")
    else:
        lines.append("- No priority fixes returned.")

    lines.extend(["", "## Next Steps"])
    lines.append("- Apply the priority fixes above.")
    lines.append(f"- Re-run `python scripts/codex_seo_machine.py optimize \"{article_path}\"` after edits.")
    if seo_result["publishing_ready"]:
        lines.append(f"- Optional publish step: `python scripts/codex_seo_machine.py publish \"{article_path}\"`.")

    return "\n".join(lines).rstrip() + "\n"


def run_context_audit(args: argparse.Namespace) -> int:
    statuses = audit_context()
    report = format_context_audit(statuses)

    if args.output:
        output = Path(args.output)
        write_text(output, report, overwrite=args.overwrite)
        print(f"context audit saved to {output}")
    else:
        print(report)
    return 0


def run_brief(args: argparse.Namespace) -> int:
    statuses = audit_context()
    output = Path(args.output) if args.output else default_brief_path(args.topic)
    report = build_brief_markdown(args.topic, statuses)
    write_text(output, report, overwrite=args.overwrite)
    print(f"research brief created at {output}")
    return 0


def run_plan(args: argparse.Namespace) -> int:
    brief_path = Path(args.brief) if args.brief else default_brief_path(args.topic)
    brief_text = read_text(brief_path)
    if not brief_text:
        raise FileNotFoundError(
            f"Research brief not found at {brief_path}. Create one with the `brief` command first."
        )

    output = Path(args.output) if args.output else default_plan_path(args.topic)
    plan_markdown = build_plan_markdown(args.topic, brief_text)
    write_text(output, plan_markdown, overwrite=args.overwrite)
    print(f"article plan created at {output}")
    return 0


def run_optimize(args: argparse.Namespace) -> int:
    components = import_optional_components()
    article_path = Path(args.article)
    original_content = load_article(article_path)

    scrubbed_content = original_content
    scrub_stats = {"unicode_removed": 0, "format_control_removed": 0, "emdashes_replaced": 0}
    if not args.no_scrub:
        scrubbed_content, scrub_stats = components["ContentScrubber"]().scrub(original_content)
        if scrubbed_content != original_content:
            article_path.write_text(scrubbed_content, encoding="utf-8")

    report = build_optimization_report(article_path, scrubbed_content, scrub_stats)
    output = Path(args.output) if args.output else default_optimize_report_path(article_path)
    write_text(output, report, overwrite=args.overwrite)
    print(f"optimization report created at {output}")
    return 0


def run_publish(args: argparse.Namespace) -> int:
    try:
        from data_sources.modules.wordpress_publisher import WordPressPublisher
    except ModuleNotFoundError as exc:
        if exc.name and not exc.name.startswith("data_sources"):
            raise MissingDependencyError(
                f"Missing dependency '{exc.name}'. Install requirements with "
                "`pip install -r data_sources/requirements.txt`."
            ) from exc
        raise

    publisher = WordPressPublisher()
    result = publisher.publish_draft(args.article, post_type=args.post_type)

    print("publish complete")
    for key in ("id", "status", "link", "edit_link"):
        if key in result:
            print(f"{key}: {result[key]}")
    return 0


def run_quartz_export(args: argparse.Namespace) -> int:
    article_path = Path(args.article)
    article_content = load_article(article_path)
    metadata = article_metadata(article_content, article_path)

    content_root = Path(args.content_dir) if args.content_dir else repo_path("site/content")
    tags = split_csv(args.tags) if args.tags else ["blog"]
    note = build_quartz_note_markdown(
        article_content=article_content,
        source_path=article_path,
        internal_domains_list=internal_domains(),
        publish=not args.draft,
        tags=tags,
    )

    output = (
        Path(args.output)
        if args.output
        else default_quartz_export_path(content_root, args.folder, metadata.slug or metadata.title)
    )
    write_text(output, note, overwrite=args.overwrite)
    print(f"quartz note exported to {output}")
    return 0


def run_quartz_install(args: argparse.Namespace) -> int:
    quartz_dir = Path(args.quartz_dir) if args.quartz_dir else default_quartz_project_dir()
    if not quartz_dir.exists():
        raise FileNotFoundError(f"Quartz project not found: {quartz_dir}")

    subprocess.run([resolve_node_executable("npm"), "ci"], cwd=quartz_dir, check=True)
    print(f"quartz dependencies installed in {quartz_dir}")
    return 0


def run_quartz_build(args: argparse.Namespace) -> int:
    quartz_dir = Path(args.quartz_dir) if args.quartz_dir else default_quartz_project_dir()
    if not quartz_dir.exists():
        raise FileNotFoundError(f"Quartz project not found: {quartz_dir}")

    content_dir = Path(args.content_dir) if args.content_dir else repo_path("site/content")
    command = build_quartz_build_args(
        content_dir=content_dir,
        output_dir=args.output_dir,
        serve=args.serve,
        watch=args.watch,
        port=args.port,
        ws_port=args.ws_port,
    )
    command[0] = resolve_node_executable("npx")
    subprocess.run(command, cwd=quartz_dir, check=True)
    print(f"quartz build complete from {content_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Codex-friendly CLI for SEO Machine workflows.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit_parser = subparsers.add_parser("context-audit", help="Check whether context files are ready.")
    audit_parser.add_argument("--output", help="Optional output path for the audit report.")
    audit_parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing output file.")
    audit_parser.set_defaults(func=run_context_audit)

    brief_parser = subparsers.add_parser("brief", help="Create a research brief scaffold.")
    brief_parser.add_argument("topic", help="Article topic.")
    brief_parser.add_argument("--output", help="Optional output path.")
    brief_parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing output file.")
    brief_parser.set_defaults(func=run_brief)

    plan_parser = subparsers.add_parser("plan", help="Create an article plan from a brief.")
    plan_parser.add_argument("topic", help="Article topic.")
    plan_parser.add_argument("--brief", help="Path to the research brief markdown file.")
    plan_parser.add_argument("--output", help="Optional output path.")
    plan_parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing output file.")
    plan_parser.set_defaults(func=run_plan)

    optimize_parser = subparsers.add_parser("optimize", help="Scrub and analyze a draft article.")
    optimize_parser.add_argument("article", help="Path to the draft markdown file.")
    optimize_parser.add_argument("--output", help="Optional output path.")
    optimize_parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing output file.")
    optimize_parser.add_argument("--no-scrub", action="store_true", help="Skip in-place scrubbing.")
    optimize_parser.set_defaults(func=run_optimize)

    publish_parser = subparsers.add_parser("publish", help="Publish a markdown draft to WordPress.")
    publish_parser.add_argument("article", help="Path to the draft markdown file.")
    publish_parser.add_argument("--post-type", default="post", help="WordPress post type. Default: post.")
    publish_parser.set_defaults(func=run_publish)

    quartz_parser = subparsers.add_parser(
        "quartz-export",
        help="Export a draft as an Obsidian/Quartz note for free web publishing workflows.",
    )
    quartz_parser.add_argument("article", help="Path to the draft markdown file.")
    quartz_parser.add_argument(
        "--content-dir",
        help="Target Obsidian vault root or Quartz content root. Defaults to site/content in this repo.",
    )
    quartz_parser.add_argument(
        "--folder",
        default="blog",
        help="Folder under the content root where the note will be written. Default: blog.",
    )
    quartz_parser.add_argument("--output", help="Optional full output path.")
    quartz_parser.add_argument("--tags", help='Comma-separated tags, for example "blog,seo,saas".')
    quartz_parser.add_argument("--draft", action="store_true", help="Export with draft: true and publish: false.")
    quartz_parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing output file.")
    quartz_parser.set_defaults(func=run_quartz_export)

    quartz_install_parser = subparsers.add_parser(
        "quartz-install",
        help="Install npm dependencies for the bundled Quartz site.",
    )
    quartz_install_parser.add_argument("--quartz-dir", help="Path to the Quartz project directory.")
    quartz_install_parser.set_defaults(func=run_quartz_install)

    quartz_build_parser = subparsers.add_parser(
        "quartz-build",
        help="Build or preview the bundled Quartz site using site/content as the source.",
    )
    quartz_build_parser.add_argument("--quartz-dir", help="Path to the Quartz project directory.")
    quartz_build_parser.add_argument(
        "--content-dir",
        help="Path to the Obsidian/Quartz content root. Defaults to site/content.",
    )
    quartz_build_parser.add_argument(
        "--output-dir",
        default="public",
        help="Quartz output directory. Default: public.",
    )
    quartz_build_parser.add_argument("--serve", action="store_true", help="Run the Quartz preview server.")
    quartz_build_parser.add_argument("--watch", action="store_true", help="Watch for file changes.")
    quartz_build_parser.add_argument("--port", type=int, help="Preview server port.")
    quartz_build_parser.add_argument("--ws-port", type=int, help="Hot reload websocket port.")
    quartz_build_parser.set_defaults(func=run_quartz_build)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except MissingDependencyError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
