"""Shared fixtures and trainer list for Playwright tests."""

from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://nachbar-blip.github.io/Mathepfade"

# Dynamisch alle HTML-Trainer aus trainer/ einlesen (90 Dateien).
_TRAINER_DIR = Path(__file__).resolve().parent.parent / "trainer"
TRAINER_FILES = sorted(p.name for p in _TRAINER_DIR.glob("*.html"))


@pytest.fixture(scope="session")
def browser():
    """Shared browser instance across all tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Fresh browser context + page per test (isoliert localStorage)."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def pytest_generate_tests(metafunc):
    """Parametrisiert alle Tests mit der Trainer-Liste."""
    if "trainer_file" in metafunc.fixturenames:
        metafunc.parametrize(
            "trainer_file",
            TRAINER_FILES,
            ids=[f.replace(".html", "") for f in TRAINER_FILES],
        )
