from time import sleep

from views.cash_payments import Login
from views.cash_payments import CashPayments



URL = "https://ai-quizwhiz.zluck.com/login"


def test_approved_filter(driver):
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

    #go to cash payment module
    cash_payments = CashPayments(driver)
    cash_payments.click_cash_payments_btn()

    # Filter Function
    cash_payments.click_approved_filter_btn()
    sleep(5)
    cash_payments.verify_approved_filter() # Verify Filter Function
    sleep(5)

def test_pending_filter(driver):
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

    # go to cash payment module
    cash_payments = CashPayments(driver)
    cash_payments.click_cash_payments_btn()

    # Filter Function
    cash_payments.click_pending_filter_btn()
    sleep(5)
    cash_payments.verify_pending_filter()  # Verify Filter Function
    sleep(5)

def test_rejected_filter(driver):
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

    # go to cash payment module
    cash_payments = CashPayments(driver)
    cash_payments.click_cash_payments_btn()

    # Filter Function
    cash_payments.click_rejected_filter_btn()
    sleep(5)
    cash_payments.verify_rejected_filter()  # Verify Filter Function
    sleep(5)

def test_reset_filter(driver):
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

    # go to cash payment module
    cash_payments = CashPayments(driver)
    cash_payments.click_cash_payments_btn()

    # Filter Function
    cash_payments.click_reset_filter_btn()
    sleep(5)
    cash_payments.verify_reset_filter()  # Verify Filter Function
    sleep(5)