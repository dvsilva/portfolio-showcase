import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class PortfolioStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "styles.css").read_text(encoding="utf-8")
        cls.js = (ROOT / "script.js").read_text(encoding="utf-8")

    def test_has_core_semantic_sections(self):
        for section_id in ("conteudo", "trabalho", "processo", "sobre", "contato"):
            self.assertIn(f'id="{section_id}"', self.html)
        self.assertIn('<main id="conteudo">', self.html)
        self.assertIn("<footer", self.html)

    def test_has_accessibility_and_resilience_markers(self):
        self.assertIn('aria-label="Navegação principal"', self.html)
        self.assertIn('aria-expanded="false"', self.html)
        self.assertIn('aria-pressed="true"', self.html)
        self.assertIn("prefers-reduced-motion", self.css)
        self.assertIn("skip-link", self.html)

    def test_progressive_enhancement_contract(self):
        self.assertGreaterEqual(self.html.count('data-category='), 3)
        self.assertIn("data-filter", self.html)
        for marker in ("aria-expanded", "is-open", "aria-pressed", "is-hidden"):
            self.assertIn(marker, self.js)

    def test_no_credential_like_content(self):
        combined = f"{self.html}\n{self.css}\n{self.js}".lower()
        self.assertNotRegex(combined, r"(api[_-]?key|secret|password)\s*[:=]")

    def test_required_assets_are_local(self):
        self.assertTrue((ROOT / "styles.css").exists())
        self.assertTrue((ROOT / "script.js").exists())
        self.assertNotIn("<img", self.html.lower())


if __name__ == "__main__":
    unittest.main()
