from time import sleep
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "data.email").clear()
        self.driver.find_element(By.ID, "data.email").send_keys(username)
        sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "data.password").clear()
        self.driver.find_element(By.ID, "data.password").send_keys(password)
        sleep(1)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button").click()
        sleep(1)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        sleep(1)

    def verify_login(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/header/div[1]/h1").text
        assert text == "Dashboard"
        sleep(3)

class CashPayments:

    def __init__(self, driver):
        self.driver = driver

    # Cash Payment Module
    def click_cash_payments_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/nav/ul/li/ul/li[7]/a").click()
        sleep(5)

    def verify_cash_payment_module(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/header/div[1]/h1").text
        assert text == "Cash Payments"
        sleep(5)

    #    Verify 'Showing X results' counter.
    def verify_showing_X_results(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/nav/span").text
        assert text == "Showing 1 to 3 of 3 results"
        sleep(5)


    # Search
    def search(self, search):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[2]/input").send_keys(search)
        sleep(3)

    # Search Plan Name
    def verify_search_plan_name(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[3]/table/tbody/tr/td[2]/div/div/div/div/div/div/span").text
        assert text == "Basic"
        sleep(3)

    #Search User Name
    def verify_user_name(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div/div/div/span").text
        assert text == "User"
        sleep(3)

    # Search with non-existent term
    def verify_non_existent(self):
        text = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[3]/div/div/h4").text
        assert text == "No Cash Payments"
        sleep(3)

    # Approved Filter
    def click_approved_filter_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/button").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]").click()
        sleep(1)

    def verify_approved_filter(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[2]/div[1]/div/span/span/span").text
        assert text == "Approved"
        sleep(3)

    # Pending Filter
    def click_pending_filter_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/button").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]").click()
        sleep(1)

    def verify_pending_filter(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[2]/div[1]/div/span/span/span").text
        assert text == "Pending"
        sleep(3)

    # Rejected Filter
    def click_rejected_filter_btn(self):
        self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/button").click()
        sleep(1)
        self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]").click()
        sleep(1)

    def verify_rejected_filter(self):
        text = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[2]/div[1]/div/span/span/span").text
        assert text == "Rejected"
        sleep(3)

    # Filter Reset Btn
    def click_reset_filter_btn(self):
        self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/button").click()
        sleep(1)
        self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/button/span").click()
        sleep(1)

    def verify_reset_filter(self):
        text = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/nav/span").text
        assert text == "Showing 1 to 3 of 3 results"
        sleep(3)


    # View Action
    def click_view_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div/button/span").click()
        sleep(5)

    def verify_view_action(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/form[2]/div/div/div[2]/div/div/div[1]/div[2]/h2").text
        assert text == "Subscription Plan Details"
        sleep(10)

        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/section/div/div/div/div/form[2]/div/div/div[2]/div/div/div[3]/div/button").click()