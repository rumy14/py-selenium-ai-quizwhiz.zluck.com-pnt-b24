from time import sleep
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(By.ID, "data.name").clear()
        self.driver.find_element(By.ID, "data.name").send_keys(name)
        sleep(1)

    def enter_email(self, email):
        self.driver.find_element(By.ID, "data.email").clear()
        self.driver.find_element(By.ID, "data.email").send_keys(email)
        sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "data.password").clear()
        self.driver.find_element(By.ID, "data.password").send_keys(password)
        sleep(1)

    def enter_confirm_password(self, c_password):
        self.driver.find_element(By.ID, "data.passwordConfirmation").clear()
        self.driver.find_element(By.ID, "data.passwordConfirmation").send_keys(c_password)
        sleep(1)

    def click_sign_up_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button").click()
        sleep(1)

    def sign_up(self, username, password,email, c_password):
        self.enter_name(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(c_password)
        self.click_sign_up_btn()
        sleep(1)

    def verify_sign_up(self):
        element = self.driver.find_element(By.CLASS_NAME, "logo-image")
        assert element.is_displayed()

        sleep(3)

    def verify_password_corfimation_erorr_message(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[3]/div/div/div[2]/p").text
        assert text == "The password field must match confirm Password:.", f"Expected 'The password field must match confirm Password:.', but got {text}"
        sleep(3)