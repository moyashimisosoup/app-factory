"""Offline tests for starter rendering. No GitHub access or credentials."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import render_starter as starter


class StarterTests(unittest.TestCase):
    def make(self, **changes):
        args = dict(app_name="小さな教材", repo_name="sample-learning-web",
                    description="スマホでも使える教材", visibility="private")
        args.update(changes)
        return starter.render(**args)

    def test_four_files_and_expected_metadata(self):
        files = self.make()
        self.assertEqual(set(files), set(starter.TEMPLATE_PATHS))
        self.assertIn("小さな教材", files["README.md"])
        self.assertIn("sample-learning-web", files["AGENTS.md"])
        self.assertIn("private", files["AGENTS.md"])
        self.assertIn('lang="ja"', files["index.html"])
        self.assertIn("prefers-reduced-motion", files["index.html"])
        self.assertIn("APP", files["AGENTS.md"])
        self.assertTrue(all("%%" not in text for text in files.values()))

    def test_html_and_markdown_escaping(self):
        files = self.make(app_name='<img src=x onerror="alert(1)">',
                          description='Text with <script>unsafe</script> & markup')
        self.assertNotIn("<img src=x", files["index.html"])
        self.assertIn("&lt;img", files["index.html"])
        self.assertNotIn("<script>unsafe", files["index.html"])
        self.assertIn("&lt;script&gt;", files["README.md"])

    def test_public_visibility_requires_explicit_argument(self):
        self.assertIn("public", self.make(visibility="public")["AGENTS.md"])
        with self.assertRaises(ValueError):
            self.make(visibility="internal")

    def test_bad_slug_and_controls_fail(self):
        for bad in ("Uppercase", "../evil", "x", "my repo", "under_score"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.make(repo_name=bad)
        for name in ("contains\nnewline", "control\x00character", ""):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.make(app_name=name)

    def test_refuses_existing_output_and_preserves_files(self):
        with TemporaryDirectory() as scratch:
            root = Path(scratch)
            dest = root / "new-starter"
            starter.write_new_directory(dest, self.make())
            self.assertTrue((dest / "index.html").exists())
            (dest / "README.md").write_text("CUSTOM", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                starter.write_new_directory(dest, self.make(app_name="new name"))
            self.assertEqual((dest / "README.md").read_text(encoding="utf-8"), "CUSTOM")

    def test_renders_without_network_or_local_repo(self):
        result = self.make()
        self.assertEqual(len(result), 4)
        self.assertIn("状態", result["README.md"])


if __name__ == "__main__":
    unittest.main()
