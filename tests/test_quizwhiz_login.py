import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_with_valid_id():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    elem_user_id_input = driver.find_element(By.XPATH, "YOUR_XPATH_HERE")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin@gmail.com")

    time.sleep(3)
    driver.quit()
