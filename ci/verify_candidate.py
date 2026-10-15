#!/usr/bin/env python3
"""Tests de confiance du pilote ; à lire depuis le commit de base, jamais la PR."""

import pathlib
import subprocess
import sys


def check(directory, arguments, expected=None, expected_exit=0):
    script = directory / "src" / "hello.py"
    assert script.is_file() and not script.is_symlink(), "SCRIPT_MISSING_OR_LINK"
    assert directory in script.resolve().parents, "SCRIPT_ESCAPES_REPO"
    assert script.stat().st_size <= 8192, "SCRIPT_TOO_LARGE"
    proc = subprocess.run(
        [sys.executable, "-I", "-B", str(script), *arguments],
        text=True, capture_output=True, timeout=8, check=False,
    )
    if expected_exit == 0:
        assert proc.returncode == 0, "SCRIPT_FAILED"
        assert proc.stderr == "", "UNEXPECTED_STDERR"
        assert proc.stdout == expected, "WRONG_OUTPUT"
    else:
        assert proc.returncode != 0, "INVALID_INPUT_ACCEPTED"


def main():
    assert len(sys.argv) == 2, "USAGE: verify_candidate.py candidate_dir"
    repo = pathlib.Path(sys.argv[1]).resolve()
    assert repo.is_dir(), "CANDIDATE_NOT_FOUND"
    check(repo, ["--name", "Élodie"], "Bonjour, Élodie!\n")
    check(repo, ["--name", "Sam", "--lang", "en"], "Hello, Sam!\n")
    check(repo, ["--name", "Zoë", "--lang", "fr"], "Bonjour, Zoë!\n")
    check(repo, [], expected_exit=1)
    check(repo, ["--name", "Sam", "--lang", "es"], expected_exit=1)
    print("KERIANH_DEMO_ORACLE=PASS; CHECKS=5; SECRETS=NONE; DEPLOYMENT=NO")


if __name__ == "__main__":
    main()
