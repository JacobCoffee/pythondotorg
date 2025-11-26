#!/usr/bin/env python3
"""Capture screenshots of Django dev server pages."""

from playwright.sync_api import sync_playwright
import sys
import os

BASE_DIR = "/Users/coffee/git/public/JacobCoffee/pythondotorg"
SCREENSHOTS_DIR = f"{BASE_DIR}/screenshots"

# Create screenshots directory if it doesn't exist
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

URLS = [
    # Main pages
    ("http://localhost:8000/", f"{SCREENSHOTS_DIR}/homepage.png"),
    ("http://localhost:8000/downloads/", f"{SCREENSHOTS_DIR}/downloads.png"),
    ("http://localhost:8000/doc/", f"{SCREENSHOTS_DIR}/docs.png"),
    ("http://localhost:8000/psf-landing/", f"{SCREENSHOTS_DIR}/psf.png"),
    ("http://localhost:8000/jobs/", f"{SCREENSHOTS_DIR}/jobs.png"),
    ("http://localhost:8000/community/", f"{SCREENSHOTS_DIR}/community.png"),
    # Blogs
    ("http://localhost:8000/blogs/", f"{SCREENSHOTS_DIR}/blogs.png"),
    # Events
    ("http://localhost:8000/events/", f"{SCREENSHOTS_DIR}/events.png"),
    ("http://localhost:8000/events/calendars/", f"{SCREENSHOTS_DIR}/events-calendars.png"),
    # Success Stories
    ("http://localhost:8000/success-stories/", f"{SCREENSHOTS_DIR}/success-stories.png"),
    ("http://localhost:8000/success-stories/submit/", f"{SCREENSHOTS_DIR}/success-stories-submit.png"),
]


def capture_screenshots():
    """Capture full-page screenshots of modernized pages."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        successful = 0
        failed = 0

        for url, screenshot_path in URLS:
            print(f"Navigating to {url}...")
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(1000)
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"  ✓ {screenshot_path.split('/')[-1]}")
                successful += 1

            except Exception as e:
                print(f"  ✗ Error: {e}", file=sys.stderr)
                failed += 1
                continue

        browser.close()
        print(f"\nDone! {successful} captured, {failed} failed")
        return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(capture_screenshots())
