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
            path = CONTENT_ROOT / locale / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md"
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
        ]

        for ko_path, en_path in pairs:
            ko_text = read_text(ko_path)
            en_text = read_text(en_path)
            self.assertEqual(frontmatter_value(ko_text, "translationKey"), frontmatter_value(en_text, "translationKey"))

    def test_model_article_references_snapshot_date(self) -> None:
        ko_text = read_text(CONTENT_ROOT / "ko" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        en_text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        self.assertIn("2025년 4월 30일", ko_text)
        self.assertIn("April 30, 2025", en_text)

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

    def test_model_article_uses_all_logo_assets(self) -> None:
        text = read_text(CONTENT_ROOT / "en" / "blog" / "ai-video" / "models" / "april-2025-ai-video-models.md")
        for name in ("openai.png", "veo.svg", "runway.svg", "kling.png", "luma.svg", "hailuo.png"):
            self.assertIn(f"assets/ai-video/model-logos/april-2025/{name}", text)


if __name__ == "__main__":
    unittest.main()
