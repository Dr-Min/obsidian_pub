import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.codex_seo_machine import (  # noqa: E402
    build_quartz_build_args,
    ContextStatus,
    build_article_metadata,
    build_brief_markdown,
    build_plan_markdown,
    build_quartz_note_markdown,
    convert_internal_markdown_links_to_wikilinks,
    default_quartz_export_path,
    extract_field,
    parse_brief,
    slugify,
)


class CodexSeoMachineTests(unittest.TestCase):
    def test_slugify_normalizes_topic(self) -> None:
        self.assertEqual(slugify("Email Marketing for SaaS"), "email-marketing-for-saas")
        self.assertEqual(slugify("  Multi   word___Topic "), "multi-word-topic")

    def test_extract_field_supports_bold_and_plain_fields(self) -> None:
        text = """
**Primary Keyword**: email marketing
Meta Title: Email Marketing Guide
"""
        self.assertEqual(extract_field(text, "Primary Keyword"), "email marketing")
        self.assertEqual(extract_field(text, "Meta Title"), "Email Marketing Guide")

    def test_parse_brief_extracts_outline_and_keywords(self) -> None:
        brief = """
## SEO Foundation
- **Primary Keyword**: onboarding email sequence
- **Secondary Keywords**: onboarding emails, lifecycle marketing

## Recommended Outline
- Introduction
- What Is an Onboarding Email Sequence?
- Best Practices

## Content Gaps & Opportunities
- Gap 1: competitors ignore churn prevention
"""
        parsed = parse_brief(brief)
        self.assertEqual(parsed["primary_keyword"], "onboarding email sequence")
        self.assertEqual(
            parsed["secondary_keywords"],
            ["onboarding emails", "lifecycle marketing"],
        )
        self.assertEqual(
            parsed["outline"],
            ["Introduction", "What Is an Onboarding Email Sequence?", "Best Practices"],
        )
        self.assertEqual(parsed["gaps"], ["Gap 1: competitors ignore churn prevention"])

    def test_build_article_metadata_prefers_brief_values(self) -> None:
        metadata = build_article_metadata(
            "Onboarding Email Sequence",
            {
                "primary_keyword": "onboarding email sequence",
                "secondary_keywords": ["user onboarding emails"],
                "meta_title": "Onboarding Email Sequence Guide",
                "meta_description": "Learn onboarding email sequence strategy.",
            },
        )
        self.assertEqual(metadata.slug, "onboarding-email-sequence")
        self.assertEqual(metadata.meta_title, "Onboarding Email Sequence Guide")
        self.assertEqual(metadata.secondary_keywords, ["user onboarding emails"])

    def test_build_brief_markdown_contains_codex_sections(self) -> None:
        statuses = [
            ContextStatus(
                key="brand_voice",
                path=REPO_ROOT / "context/brand-voice.md",
                ready=False,
                notes=["template marker present: [YOUR COMPANY]"],
            )
        ]
        markdown = build_brief_markdown("Email Marketing for SaaS", statuses)
        self.assertIn("# Research Brief: Email Marketing for SaaS", markdown)
        self.assertIn("## Recommended Outline", markdown)
        self.assertIn("## Codex Notes", markdown)

    def test_build_plan_markdown_contains_writing_prompts(self) -> None:
        brief = """
## SEO Foundation
- **Primary Keyword**: email marketing for saas
- **Secondary Keywords**: lifecycle email, saas onboarding

## Recommended Outline
- Introduction
- What Is Email Marketing for SaaS?
- Best Practices for Email Marketing for SaaS
- Frequently Asked Questions
- Conclusion

## Content Gaps & Opportunities
- Gap 1: include renewal examples

## Unique Insights to Use
- Insight 1: compare onboarding and expansion campaigns

## Internal Link Candidates
- Pricing page - https://example.com/pricing
"""
        markdown = build_plan_markdown("Email Marketing for SaaS", brief)
        self.assertIn("# Article Plan: Email Marketing for SaaS", markdown)
        self.assertIn("## Section Writing Prompts", markdown)
        self.assertIn("Prompt for Section 1", markdown)
        self.assertIn("Draft file name:", markdown)

    def test_convert_internal_markdown_links_to_wikilinks(self) -> None:
        body = (
            "Read [Retention Playbook](https://notes.example.com/blog/retention-playbook) "
            "and [Onboarding](https://notes.example.com/blog/onboarding#setup). "
            "Keep [External](https://google.com) unchanged."
        )
        converted = convert_internal_markdown_links_to_wikilinks(
            body,
            ["notes.example.com"],
        )
        self.assertIn("[[retention-playbook|Retention Playbook]]", converted)
        self.assertIn("[[onboarding#setup|Onboarding]]", converted)
        self.assertIn("[External](https://google.com)", converted)

    def test_build_quartz_note_markdown_adds_frontmatter_and_strips_metadata(self) -> None:
        article = """
# Email Marketing for SaaS

**Meta Title**: Email Marketing for SaaS Guide
**Meta Description**: Learn lifecycle email strategy.
**Primary Keyword**: email marketing for saas
**Secondary Keywords**: lifecycle email, onboarding email
**URL Slug**: /blog/email-marketing-for-saas

---

See [Retention Playbook](https://notes.example.com/blog/retention-playbook).

## Why it matters

Body text.
"""
        note = build_quartz_note_markdown(
            article_content=article,
            source_path=REPO_ROOT / "drafts/email-marketing-for-saas-2026-04-10.md",
            internal_domains_list=["notes.example.com"],
            publish=True,
            tags=["blog", "saas"],
        )
        self.assertIn('title: "Email Marketing for SaaS"', note)
        self.assertIn('description: "Learn lifecycle email strategy."', note)
        self.assertIn("draft: false", note)
        self.assertIn("publish: true", note)
        self.assertIn("- blog", note)
        self.assertIn("[[retention-playbook|Retention Playbook]]", note)
        self.assertNotIn("**Meta Title**:", note)
        self.assertNotIn("# Email Marketing for SaaS", note)

    def test_default_quartz_export_path_uses_blog_folder_and_slug(self) -> None:
        output = default_quartz_export_path(
            REPO_ROOT / "site/content",
            "blog",
            "Email Marketing for SaaS",
        )
        self.assertEqual(
            output,
            REPO_ROOT / "site/content/blog/email-marketing-for-saas.md",
        )

    def test_build_quartz_build_args_for_serve_mode(self) -> None:
        args = build_quartz_build_args(
            content_dir=REPO_ROOT / "site/content",
            output_dir="public",
            serve=True,
            watch=True,
            port=8088,
            ws_port=3010,
        )
        self.assertEqual(args[:2], ["npx", "quartz"])
        self.assertIn("--serve", args)
        self.assertIn("--watch", args)
        self.assertIn("-d", args)
        self.assertIn(str(REPO_ROOT / "site/content"), args)
        self.assertIn("--port", args)
        self.assertIn("8088", args)
        self.assertIn("--wsPort", args)
        self.assertIn("3010", args)


if __name__ == "__main__":
    unittest.main()
