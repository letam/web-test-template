def test_visit_google_com_returns_page_with_Google_in_title(browser):
    b = browser
    b.visit("https://www.google.com/")
    assert "Google" in b.title


def test_wait_for(browser):
    b = browser
    b.visit("https://www.google.com/")
    b.fill("q", "github")
    search_button = b.find_by_name("btnK")
    b.wait_for(search_button.is_displayed, timeout=1.5)


def test_wait_for_not(browser):
    b = browser
    b.visit("https://www.google.com/")
    b.fill("q", "github")
    search_button = b.find_by_name("btnK")
    b.wait_for_not(search_button.is_displayed)


def test_wait_for_not_and_wait_for_back_and_forth(browser):
    b = browser
    b.visit("https://www.google.com/")
    b.fill("q", "github")
    search_button = b.find_by_name("btnK")
    b.wait_for_not(search_button.is_displayed)
    b.wait_for(search_button.is_displayed)
    b.execute_script("document.querySelector(\"input[name='btnK']\").hidden = true")
    b.wait_for_not(search_button.is_displayed)
    b.execute_script("document.querySelector(\"input[name='btnK']\").hidden = false")
    b.wait_for(search_button.is_displayed)


def test_fill_github_in_google_search_box_returns_github_website(browser):
    b = browser
    b.visit("https://www.google.com/")
    b.fill("q", "github")
    search_button = b.find_by_name("btnK")
    b.wait_for(search_button.is_displayed, timeout=1.5)
    search_button.click()
    b.wait(1)
    assert b.find_by_text("github.com")
