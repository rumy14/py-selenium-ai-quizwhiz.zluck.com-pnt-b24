from time import sleep

# from views.login import LoginPage
from views.faqs import HomePage


URL = "https://ai-quizwhiz.zluck.com"


# def test_login(driver):
def test_homepage(driver):
    # Initialize Page Objects
    home_page = HomePage(driver)

    # Open Webpage
    driver.get(URL)
"""
    # Login
    username = "admin@gmail.com"
    password = "123456"
    login_page.login(username, password)
    sleep(5)

    login_page.verify_login()  # Verify Login Page
"""
