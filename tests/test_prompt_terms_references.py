import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPT_TERMS_ROOT = REPO_ROOT / "site" / "content"
LOCALES = ("ko", "en")
SUMMARY_HEADINGS = {"summary", "정리"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def prompt_terms_dir(locale: str) -> Path:
    return PROMPT_TERMS_ROOT / locale / "blog" / "ai-video" / "prompt-terms"


def parse_frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"([^\"]+)\"\s*$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    match = re.search(rf"^{re.escape(key)}:\s*([^\n]+)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def iter_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        heading = match.group(1).strip()
        body = text[start:end]
        sections.append((heading, body))
    return sections


def extract_image_refs(text: str) -> list[str]:
    refs: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("!["):
            continue

        wiki_match = re.search(r"!\[\[(.+?)\]\]", line)
        if wiki_match:
            refs.append(wiki_match.group(1).split("|", 1)[0].strip())
            continue

        angle_match = re.search(r"!\[[^\]]*\]\(<([^>]+)>\)", line)
        if angle_match:
            refs.append(angle_match.group(1).strip())
            continue

        plain_match = re.search(r"!\[[^\]]*\]\((.+)\)$", line)
        if plain_match:
            refs.append(plain_match.group(1).strip())

    return refs


class PromptTermsReferenceTests(unittest.TestCase):
    def test_prompt_terms_have_ko_en_counterparts(self) -> None:
        per_locale = {}
        for locale in LOCALES:
            base = prompt_terms_dir(locale)
            categories = {path.parent.name for path in base.glob("*/index.md")}
            per_locale[locale] = categories

        self.assertEqual(per_locale["ko"], per_locale["en"])
        for category in sorted(per_locale["ko"]):
            for locale in LOCALES:
                path = prompt_terms_dir(locale) / category / "index.md"
                self.assertTrue(path.exists(), f"missing prompt-terms page: {path}")

    def test_prompt_terms_do_not_use_svg_placeholders(self) -> None:
        for locale in LOCALES:
            for path in sorted(prompt_terms_dir(locale).glob("*/index.md")):
                text = read_text(path)
                self.assertNotIn("assets/ai-video/glossary/", text, f"placeholder glossary asset remains in {path}")
                for ref in extract_image_refs(text):
                    self.assertFalse(ref.lower().endswith(".svg"), f"svg image reference remains in {path}: {ref}")

    def test_each_non_summary_section_has_images_and_unique_refs(self) -> None:
        for locale in LOCALES:
            for path in sorted(prompt_terms_dir(locale).glob("*/index.md")):
                text = read_text(path)
                seen: set[str] = set()

                for heading, body in iter_sections(text):
                    if heading.strip().lower() in SUMMARY_HEADINGS:
                        continue

                    refs = extract_image_refs(body)
                    self.assertTrue(refs, f"section '{heading}' in {path} has no image reference")
                    for ref in refs:
                        self.assertNotIn(ref, seen, f"duplicate image reference in {path}: {ref}")
                        seen.add(ref)

    def test_ko_en_pages_share_translation_keys(self) -> None:
        for ko_path in sorted(prompt_terms_dir("ko").glob("*/index.md")):
            en_path = prompt_terms_dir("en") / ko_path.parent.name / "index.md"
            ko_text = read_text(ko_path)
            en_text = read_text(en_path)
            ko_key = parse_frontmatter_value(ko_text, "translationKey")
            en_key = parse_frontmatter_value(en_text, "translationKey")
            self.assertTrue(ko_key, f"missing translationKey in {ko_path}")
            self.assertEqual(
                ko_key,
                en_key,
                f"translationKey mismatch between {ko_path} and {en_path}",
            )


if __name__ == "__main__":
    unittest.main()
