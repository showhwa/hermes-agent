"""Regression tests for Docker stage2 browser executable discovery."""

from pathlib import Path


def test_stage2_discovers_cloakbrowser_and_headless_shell_basenames() -> None:
    """Discovery accepts both CloakBrowser and Chromium shell basenames."""
    script = Path("docker/stage2-hook.sh").read_text(encoding="utf-8")

    assert "-name 'cloakbrowser'" in script
    assert "-name 'headless_shell'" in script


def test_stage2_discovery_stays_filename_matched() -> None:
    """Avoid broad path grep that can pick executable shared libraries."""
    script = Path("docker/stage2-hook.sh").read_text(encoding="utf-8")

    discovery_block = script.split("browser_bin=$(", 1)[1].split(")\n    if", 1)[0]
    assert "find \"$CLOAKBROWSER_ROOT\" -type f -executable" in discovery_block
    assert "grep" not in discovery_block
