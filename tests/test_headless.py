from playwright.sync_api import sync_playwright

def test_headless_execution():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.set_content("""
            <html>
                <title>CI Test</title>
                <h1>Focus Bear Testing</h1>
            </html>
        """)

        assert page.title() == "CI Test"

        assert page.locator("h1").inner_text() == "Focus Bear Testing"

        browser.close()