import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Test Case_1 login_with_valid Credetial---
def test_login_with_valid_id():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin@gmail.com")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("Custom message: Login successful with valid credentials.")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

#Test Case_2 login with valid Username and ivalid password--
def test_login_with_valid_Username_and_ivalidpassword():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin@gmail.com")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("1234568")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("These credentials do not match our records.")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_3 login with invalid Username and valid Password---
def test_login_with_invalid_Username_and_validPassword():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    # Test Case_3 login_with_valid user invalid password--------

    # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin1@gmail.com")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("These credentials do not match our records.")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_4 login_with_ivalid_username_and_invalid_password

def test_login_with_invalid_Username_and_ivalid_Password():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin1@gmail.com")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456S")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("These credentials do not match our records.")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_5 login_with_username_field_blank--
def test_login_with_userid_blank_and_validpassword():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

   # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456S")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("please fill out this field..")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_6 login_with_password-field_blank--
def test_login_with_valid_userid_and_password_blank():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

   # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin@gmail.com")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("please fill out this field.")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_7 login_with_mandatory_fields_are_empty--
def test_login_with_mandatory_fields_are_empty():

    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("")
    time.sleep(3)

    # Click Login
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("please fill out this field.")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_9 login_password_field_masks_the_entered_characters--
def test_login_with_password_field_masks ():

    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

    # Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin@gmail.com")
    time.sleep(3)

    # Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.quit()

# Test Case_10 Forget_password_link-
def test_Forget_password_link():

        driver = webdriver.Chrome()
        driver.get("https://ai-quizwhiz.zluck.com/login")
        driver.maximize_window()

        elem_Forgot_Password = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[1]/div/span/a/span")
        elem_Forgot_Password.click()
        driver.implicitly_wait(5)
        time.sleep(5)
        driver.quit()

# Test Case_11 Logout_ends_session-
def test_Logout_ends_session():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Username
    elem_user_id_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_user_id_input.clear()
    elem_user_id_input.send_keys("admin@gmail.com")
    time.sleep(3)

# Password
    elem_pass_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")
    time.sleep(3)

# Click Login_btn
    elem_btn_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()
    print("Custom message: Login successful with valid credentials.")
    time.sleep(5)

# Click profile admin
    elem_super_admin = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/nav/div/div[2]/div[1]/div/p[1]")
    elem_super_admin.click()
    time.sleep(5)

# Click loguot
    elem_logout = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/nav/div/div[2]/div[2]/div[3]/form/button/span")
    elem_logout.click()
    time.sleep(5)
    driver.implicitly_wait(5)
    driver.quit()

