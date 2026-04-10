import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = REPO_ROOT / "site" / "content"
QUARTZ_CONFIG = REPO_ROOT / "site" / "quartz-site" / "quartz.config.ts"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"([^\"]+)\"\s*$", text, re.MULTILINE)
    if match:
        return match.group(1)
    match = re.search(rf"^{re.escape(key)}:\s*([^\n]+)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


class SiteInfoPageTests(unittest.TestCase):
    def test_quartz_base_url_defaults_to_minventory_domain(self) -> None:
        config = read_text(QUARTZ_CONFIG)
        self.assertIn('baseUrl: process.env.QUARTZ_BASE_URL ?? "minventory.org"', config)

    def test_bilingual_info_pages_exist(self) -> None:
        for slug in ("about", "privacy", "contact"):
            for locale in ("ko", "en"):
                path = CONTENT_ROOT / locale / slug / "index.md"
                self.assertTrue(path.exists(), f"missing page: {path}")

    def test_bilingual_info_pages_share_translation_keys(self) -> None:
        for slug in ("about", "privacy", "contact"):
            ko_path = CONTENT_ROOT / "ko" / slug / "index.md"
            en_path = CONTENT_ROOT / "en" / slug / "index.md"
            ko_text = read_text(ko_path)
            en_text = read_text(en_path)
            self.assertEqual(frontmatter_value(ko_text, "translationKey"), frontmatter_value(en_text, "translationKey"))

    def test_contact_pages_reference_minventory_email(self) -> None:
        for locale in ("ko", "en"):
            path = CONTENT_ROOT / locale / "contact" / "index.md"
            text = read_text(path)
            self.assertIn("contact@minventory.org", text)


if __name__ == "__main__":
    unittest.main()
