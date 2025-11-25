#!/usr/bin/env python3
"""Capture screenshots of Django dev server pages."""

from playwright.sync_api import sync_playwright
import sys

BASE_DIR = "/Users/coffee/git/public/JacobCoffee/pythondotorg"

URLS = [
    ("http://localhost:8000/", f"{BASE_DIR}/screenshot-homepage.png"),
    ("http://localhost:8000/downloads/", f"{BASE_DIR}/screenshot-downloads.png"),
    ("http://localhost:8000/psf-landing/", f"{BASE_DIR}/screenshot-psf.png"),
    ("http://localhost:8000/jobs/", f"{BASE_DIR}/screenshot-jobs.png"),
    ("http://localhost:8000/community/", f"{BASE_DIR}/screenshot-community.png"),
]


def capture_screenshots():
    """Capture full-page screenshots of modernized pages."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        for url, screenshot_path in URLS:
            print(f"Navigating to {url}...")
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(1000)
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"✓ {screenshot_path.split('/')[-1]}")

            except Exception as e:
                print(f"✗ Error capturing {url}: {e}", file=sys.stderr)
                browser.close()
                return 1

        browser.close()
        print("\n✓ All screenshots captured successfully!")
        return 0


if __name__ == "__main__":
    sys.exit(capture_screenshots())
