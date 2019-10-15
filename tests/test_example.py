def test_visit_google_com_returns_page_with_Google_in_title(browser):
    b = browser
    b.visit("https://www.google.com/")
    assert "Google" in b.title


def test_chrome_fill_github_in_google_search_box_returns_github_website(chrome_browser):
    b = chrome_browser
    b.visit("https://www.google.com/")
    b.fill("q", "github")
    search_button = b.find_by_name("btnK")
    b.wait_for(search_button.is_displayed, timeout=1.5)
    search_button.click()
    b.wait(1)
    assert b.find_by_text("github.com")
