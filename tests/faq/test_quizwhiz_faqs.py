#from selenium import webdriver
#from selenium.webdriver.common.by import By

from time import sleep
from views.faq.faqs import HomePage

URL = "https://ai-quizwhiz.zluck.com"
#home_page = HomePage(driver)

def test_homepage(driver):
    # Initialize Page Objects
    # open the Webpage
    driver.get(URL)

    # Find the login button and clicking on it to open the login page

    home_page = HomePage(driver)
    #home_page.homepage_login_btn()
    assert home_page.homepage_login_btn() is True

    sleep(5)


    # Performing User Login in Log in page with email and password
    #def test_user_login(driver):

    username = "admin@gmail.com"
    password = "123456"
    #home_page.login(username, password)
    assert home_page.login(username, password) is True
    sleep(5)


    # Varifying displayed Admin page after successful login

    varify_text = home_page.verify_login()
    print(varify_text)
    assert varify_text == "Dashboard", f"Expected 'Dashboard', but got {varify_text}"
    sleep(5)

    # Opening General settings page after finding setting button and clicking on it

    assert home_page.general_settings() is True
    sleep(5)

    # Displaying FAQ page for searching and creating new faqs

    assert home_page.faqs_paging() is True
    sleep(5)

    # Searching FAQ item
    search = "What is AI QuizWhiz?"
    assert home_page.faqs_searching(search) is True
    sleep(5)


    # Adding FAQ items

    question ="What kind of service is available?"
    answer ="AI generated questions and answers"
    assert home_page.faqs_new() is True
    sleep(5)
    assert home_page.faqs_adding(question, answer) is True

    sleep(5)



