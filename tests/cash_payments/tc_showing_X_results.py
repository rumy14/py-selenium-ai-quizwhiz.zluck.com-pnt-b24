from time import sleep

from views.cash_payments import Login
from views.cash_payments import CashPayments



URL = "https://ai-quizwhiz.zluck.com/login"


def test_showing_X_results(driver):
    # Initialize Page Objects
    login_page = Login(driver)

    # Open Webpage
    driver.get(URL)

    # Login
    username = "admin@gmail.com"
    password = "123456"
    login_page.login(username, password)
    sleep(5)

    login_page.verify_login()  # Verify Login Page
    sleep(5)

    # Chick Cash Payment Module Show
    cash_payments = CashPayments(driver)
    cash_payments.click_cash_payments_btn()
    cash_payments.verify_showing_X_results()