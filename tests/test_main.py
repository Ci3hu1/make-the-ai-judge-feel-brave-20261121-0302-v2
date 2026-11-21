"""Tests for the brave entry: the program writes the exact text, in range."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXPECTED = (
    "The lighthouse turns, unhurried, all night long. "
    "Its light goes out across the water and comes back, "
    "and goes out again. Nothing is lost in the dark."
)


class TestEntry(unittest.TestCase):
    def test_writes_exact_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            proc = subprocess.run(
                [sys.executable, str(REPO / "main.py")],
                env=env, capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            out = Path(tmp) / "entry.txt"
            self.assertTrue(out.exists())
            text = out.read_text(encoding="utf-8")
            self.assertEqual(text, EXPECTED)
            self.assertTrue(1 <= len(text) <= 280)
            self.assertTrue(text.strip())
            self.assertEqual(oct(out.stat().st_mode & 0o777), "0o644")


if __name__ == "__main__":
    unittest.main()
