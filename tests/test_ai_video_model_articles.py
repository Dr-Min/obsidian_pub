import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = REPO_ROOT / "site" / "content"
ASSET_ROOT = CONTENT_ROOT / "assets" / "ai-video" / "model-logos" / "april-2025"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"([^\"]+)\"\s*$", text, re.MULTILINE)
    if match:
        return match.group(1)
    match = re.search(rf"^{re.escape(key)}:\s*([^\n]+)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


class AiVideoModelArticleTests(unittest.TestCase):
    def test_model_indexes_exist_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            path = CONTENT_ROOT / locale / "blog" / "ai-video" / "models" / "index.md"
            self.assertTrue(path.exists(), f"missing model index: {path}")

    def test_model_articles_exist_in_both_languages(self) -> None:
        for locale in ("ko", "en"):
            for name in (
                "april-2025-ai-video-models.md",
                "april-2026-ai-video-models.md",
                "pika-separate-category.md",
            ):
                path = CONTENT_ROOT / locale / "blog" / "ai-video" / "models" / name
                self.assertTrue(path.exists(), f"missing model article: {path}")

    def test_model_pages_share_translation_keys(self) -> None:
        pairs = [
            (
                CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "index.md",
                CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "index.md",
            ),
            (
                CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md",
                CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md",
            ),
            (
                CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md",
                CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md",
            ),
            (
                CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "pika-separate-category.md",
                CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "pika-separate-category.md",
            ),
        ]

        for ko_path, en_path in pairs:
            ko_text = read_text(ko_path)
            en_text = read_text(en_path)
            self.assertEqual(frontmatter_value(ko_text, "translationKey"), frontmatter_value(en_text, "translationKey"))

    def test_april_2025_article_references_snapshot_date(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        self.assertIn("2025", ko_text)
        self.assertIn("April 30, 2025", en_text)

    def test_april_2026_article_references_snapshot_date(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md")
        self.assertEqual(frontmatter_value(ko_text, "date"), "2026-04-10")
        self.assertIn("April 10, 2026", en_text)

    def test_model_logo_assets_exist(self) -> None:
        expected = {
            "openai.png",
            "veo.svg",
            "runway.svg",
            "kling.png",
            "luma.svg",
            "hailuo.png",
        }
        actual = {path.name for path in ASSET_ROOT.glob("*")}
        self.assertTrue(expected.issubset(actual), f"missing logo assets: {sorted(expected - actual)}")

    def test_april_2025_model_article_uses_expected_logos(self) -> None:
        text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        for name in ("openai.png", "veo.svg", "runway.svg", "kling.png", "luma.svg", "hailuo.png"):
            self.assertIn(f"assets/ai-video/model-logos/april-2025/{name}", text)

    def test_april_2026_model_article_uses_current_logos(self) -> None:
        text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md")
        for name in ("openai.png", "veo.svg", "runway.svg", "kling.png", "luma.svg", "hailuo.png"):
            self.assertIn(f"assets/ai-video/model-logos/april-2025/{name}", text)
        self.assertIn("favicon_1/favicon.ico", text)

    def test_pika_note_is_linked_from_model_pages(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "index.md")
        ko_2025 = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        en_2025 = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        ko_2026 = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md")
        en_2026 = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2026-ai-video-models.md")

        self.assertIn("pika-separate-category", ko_index)
        self.assertIn("pika-separate-category", en_index)
        self.assertIn("pika-separate-category", ko_2025)
        self.assertIn("pika-separate-category", en_2025)
        self.assertIn("pika-separate-category", ko_2026)
        self.assertIn("pika-separate-category", en_2026)

    def test_current_snapshot_is_linked_from_model_indexes(self) -> None:
        ko_index = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "index.md")
        en_index = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "index.md")

        self.assertIn("april-2026-ai-video-models", ko_index)
        self.assertIn("april-2026-ai-video-models", en_index)


if __name__ == "__main__":
    unittest.main()
