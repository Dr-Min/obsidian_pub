import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = REPO_ROOT / "site" / "content"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"([^\"]+)\"\s*$", text, re.MULTILINE)
    if match:
        return match.group(1)
    match = re.search(rf"^{re.escape(key)}:\s*([^\n]+)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


class SeedanceArchiveTests(unittest.TestCase):
    def test_new_seedance_archive_exists_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            path = (
                CONTENT_ROOT
                / locale
                / "blog"
                / "ai-video"
                / "seedance"
                / "anime-nyc-giant-monster-punch-prompt.md"
            )
            self.assertTrue(path.exists(), f"missing Seedance archive: {path}")

    def test_new_seedance_archive_shares_translation_key(self) -> None:
        ko_path = CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "anime-nyc-giant-monster-punch-prompt.md"
        en_path = CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "anime-nyc-giant-monster-punch-prompt.md"
        ko_text = read_text(ko_path)
        en_text = read_text(en_path)

        self.assertEqual(
            frontmatter_value(ko_text, "translationKey"),
            frontmatter_value(en_text, "translationKey"),
        )

    def test_new_seedance_archive_is_linked_from_indexes(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "index.md")

        self.assertIn("anime-nyc-giant-monster-punch-prompt", ko_index)
        self.assertIn("anime-nyc-giant-monster-punch-prompt", en_index)

    def test_new_seedance_archive_mentions_model_and_structure(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "anime-nyc-giant-monster-punch-prompt.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "anime-nyc-giant-monster-punch-prompt.md")

        self.assertIn("Seedance 2.0", ko_text)
        self.assertIn("5 cuts / 15 seconds", ko_text)
        self.assertIn("Seedance 2.0", en_text)
        self.assertIn("5 cuts / 15 seconds", en_text)

    def test_dark_warrior_archive_exists_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            path = (
                CONTENT_ROOT
                / locale
                / "blog"
                / "ai-video"
                / "seedance"
                / "dark-warrior-red-moon-temple-clash-prompt.md"
            )
            self.assertTrue(path.exists(), f"missing Seedance archive: {path}")

    def test_dark_warrior_archive_shares_translation_key(self) -> None:
        ko_path = CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "dark-warrior-red-moon-temple-clash-prompt.md"
        en_path = CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "dark-warrior-red-moon-temple-clash-prompt.md"
        ko_text = read_text(ko_path)
        en_text = read_text(en_path)

        self.assertEqual(
            frontmatter_value(ko_text, "translationKey"),
            frontmatter_value(en_text, "translationKey"),
        )

    def test_dark_warrior_archive_is_linked_from_indexes(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "index.md")

        self.assertIn("dark-warrior-red-moon-temple-clash-prompt", ko_index)
        self.assertIn("dark-warrior-red-moon-temple-clash-prompt", en_index)

    def test_dark_warrior_archive_mentions_model_and_structure(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "dark-warrior-red-moon-temple-clash-prompt.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "dark-warrior-red-moon-temple-clash-prompt.md")

        self.assertIn("Seedance 2.0", ko_text)
        self.assertIn("4 scenes / 15 seconds", ko_text)
        self.assertIn("Seedance 2.0", en_text)
        self.assertIn("4 scenes / 15 seconds", en_text)

    def test_anime_swordswoman_archive_exists_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            path = (
                CONTENT_ROOT
                / locale
                / "blog"
                / "ai-video"
                / "seedance"
                / "anime-swordswoman-crimson-moon-temple-clash-prompt.md"
            )
            self.assertTrue(path.exists(), f"missing Seedance archive: {path}")

    def test_anime_swordswoman_archive_shares_translation_key(self) -> None:
        ko_path = CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "anime-swordswoman-crimson-moon-temple-clash-prompt.md"
        en_path = CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "anime-swordswoman-crimson-moon-temple-clash-prompt.md"
        ko_text = read_text(ko_path)
        en_text = read_text(en_path)

        self.assertEqual(
            frontmatter_value(ko_text, "translationKey"),
            frontmatter_value(en_text, "translationKey"),
        )

    def test_anime_swordswoman_archive_is_linked_from_indexes(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "index.md")

        self.assertIn("anime-swordswoman-crimson-moon-temple-clash-prompt", ko_index)
        self.assertIn("anime-swordswoman-crimson-moon-temple-clash-prompt", en_index)

    def test_anime_swordswoman_archive_mentions_model_and_structure(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "anime-swordswoman-crimson-moon-temple-clash-prompt.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "anime-swordswoman-crimson-moon-temple-clash-prompt.md")

        self.assertIn("Seedance 2.0", ko_text)
        self.assertIn("4 scenes / 15 seconds", ko_text)
        self.assertIn("Seedance 2.0", en_text)
        self.assertIn("4 scenes / 15 seconds", en_text)

    def test_noir_western_archive_exists_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            path = (
                CONTENT_ROOT
                / locale
                / "blog"
                / "ai-video"
                / "seedance"
                / "noir-western-saloon-madam-cowboy-lighter-transition-prompt.md"
            )
            self.assertTrue(path.exists(), f"missing Seedance archive: {path}")

    def test_noir_western_archive_shares_translation_key(self) -> None:
        ko_path = CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "noir-western-saloon-madam-cowboy-lighter-transition-prompt.md"
        en_path = CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "noir-western-saloon-madam-cowboy-lighter-transition-prompt.md"
        ko_text = read_text(ko_path)
        en_text = read_text(en_path)

        self.assertEqual(
            frontmatter_value(ko_text, "translationKey"),
            frontmatter_value(en_text, "translationKey"),
        )

    def test_noir_western_archive_is_linked_from_indexes(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "index.md")

        self.assertIn("noir-western-saloon-madam-cowboy-lighter-transition-prompt", ko_index)
        self.assertIn("noir-western-saloon-madam-cowboy-lighter-transition-prompt", en_index)

    def test_noir_western_archive_mentions_model_structure_and_reference_note(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "noir-western-saloon-madam-cowboy-lighter-transition-prompt.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "noir-western-saloon-madam-cowboy-lighter-transition-prompt.md")

        self.assertIn("Seedance 2.0", ko_text)
        self.assertIn("3 cuts / transition sequence", ko_text)
        self.assertIn("P8wryMbw_Qg", ko_text)
        self.assertIn("Seedance 2.0", en_text)
        self.assertIn("3 cuts / transition sequence", en_text)

    def test_cctv_cat_archive_exists_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            path = (
                CONTENT_ROOT
                / locale
                / "blog"
                / "ai-video"
                / "seedance"
                / "cctv-trumpet-cat-midnight-wakeup-prompt.md"
            )
            self.assertTrue(path.exists(), f"missing Seedance archive: {path}")

    def test_cctv_cat_archive_shares_translation_key(self) -> None:
        ko_path = CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "cctv-trumpet-cat-midnight-wakeup-prompt.md"
        en_path = CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "cctv-trumpet-cat-midnight-wakeup-prompt.md"
        ko_text = read_text(ko_path)
        en_text = read_text(en_path)

        self.assertEqual(
            frontmatter_value(ko_text, "translationKey"),
            frontmatter_value(en_text, "translationKey"),
        )

    def test_cctv_cat_archive_is_linked_from_indexes(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "index.md")

        self.assertIn("cctv-trumpet-cat-midnight-wakeup-prompt", ko_index)
        self.assertIn("cctv-trumpet-cat-midnight-wakeup-prompt", en_index)

    def test_cctv_cat_archive_mentions_model_structure_and_negative_prompt(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "seedance" / "cctv-trumpet-cat-midnight-wakeup-prompt.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "seedance" / "cctv-trumpet-cat-midnight-wakeup-prompt.md")

        self.assertIn("Seedance 2.0", ko_text)
        self.assertIn("single shot / 10 seconds", ko_text)
        self.assertIn("ytEMzCCC7Y8", ko_text)
        self.assertIn("cat on all fours", ko_text)
        self.assertIn("Seedance 2.0", en_text)
        self.assertIn("single shot / 10 seconds", en_text)
        self.assertIn("Negative prompt", en_text)
        self.assertIn("Paranormal Activity atmosphere", en_text)


if __name__ == "__main__":
    unittest.main()
