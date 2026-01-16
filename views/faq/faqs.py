#from pycparser.c_ast import Return
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def homepage_login_btn(self):

        self.driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/div[2]/a[1]").click()
        #sleep(1)
        return True

    def enter_username(self, username):
        self.driver.find_element(By.ID, "data.email").clear()
        self.driver.find_element(By.ID, "data.email").send_keys(username)
        #sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "data.password").clear()
        self.driver.find_element(By.ID, "data.password").send_keys(password)
        #sleep(1)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button").click()
        #sleep(1)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        #sleep(1)
        return True

    def verify_login(self):

        ver_text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/header/div[1]/h1").text
        return ver_text

    def general_settings(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/nav/ul/li/ul/li[12]/a").click()
        return True
        #pass

    def faqs_paging(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div[4]/ul/li/ul/li[8]/a").click()
        return True

    def faqs_searching(self,search):
       # pass
        self.driver.find_element(By.ID, "input-1").clear()
        self.driver.find_element(By.ID, "input-1").send_keys(search)
        return True

    def faqs_new(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/header/div[2]/div/button").click()
        return True

    def faqs_adding(self,question, answer):

        self.driver.find_element(By.ID, "mountedActionsData.0.question").clear()
        self.driver.find_element(By.ID, "mountedActionsData.0.question").send_keys(question)
        self.driver.find_element(By.ID, "mountedActionsData.0.answer").clear()
        self.driver.find_element(By.ID, "mountedActionsData.0.answer").send_keys(answer)

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/div/div[5]/div/div/form[1]/div/div/div[2]/div/div/div[3]/div/button[1]").click()
        return True
