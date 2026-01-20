import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Test Case_1 Navigate to registration page URL---
def test_website_login():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Sign up
    elem_sign_up = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/div[2]/a")
    elem_sign_up.click()
    time.sleep(3)
    print("successfully login.")
    driver.implicitly_wait(5)
    driver.quit()

#Test Case_2 Verify all input fields accept valid data---
def test_login_with_valid_input ():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Sign up
    elem_sign_up = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/div[2]/a")
    elem_sign_up.click()
    time.sleep(3)

# Name input
    elem_user_name_input = driver.find_element(By.ID,"data.name")
    elem_user_name_input.clear()
    elem_user_name_input.send_keys("nadira")
    time.sleep(3)

#Email Address input
    elem_user_email_input = driver.find_element(By.ID, "data.email")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("nadira.p1999@gmail.com")
    time.sleep(3)

#Password
    elem_user_email_input = driver.find_element(By.ID, "data.password")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)

#Confirm Password
    elem_user_email_input = driver.find_element(By.ID, "data.passwordConfirmation")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)
# Sign up button click
    elem_sign_up_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button/span[1]")
    elem_sign_up_login.click()
    print("Custom message: Login successful with valid credentials.")
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.quit()

#Test Case_3 Verify all input fields empty
def test_login_with_mandatory_field_empty ():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Sign up
    elem_sign_up = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/div[2]/a")
    elem_sign_up.click()
    time.sleep(3)

# Name input
    elem_user_name_input = driver.find_element(By.ID,"data.name")
    elem_user_name_input.clear()
    elem_user_name_input.send_keys("")
    time.sleep(3)

#Email Address input
    elem_user_email_input = driver.find_element(By.ID, "data.email")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("")
    time.sleep(3)

#Password
    elem_user_email_input = driver.find_element(By.ID, "data.password")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("")
    time.sleep(3)

#Confirm Password
    elem_user_email_input = driver.find_element(By.ID, "data.passwordConfirmation")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("")
    time.sleep(3)
# Sign up button click
    elem_sign_up_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button/span[1]")
    elem_sign_up_login.click()
    time.sleep(3)
    print("please fill out this field.")
    driver.implicitly_wait(5)
    driver.quit()

#Test Case_4 Verify all input fields empty
def test_login_with_invalid_email  ():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Sign up
    elem_sign_up = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/div[2]/a")
    elem_sign_up.click()
    time.sleep(3)

# Name input
    elem_user_name_input = driver.find_element(By.ID,"data.name")
    elem_user_name_input.clear()
    elem_user_name_input.send_keys("Nadira")
    time.sleep(3)

#Email Address invalidinput
    elem_user_email_input = driver.find_element(By.ID, "data.email")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("testgmail.com")
    time.sleep(3)

#Password
    elem_user_email_input = driver.find_element(By.ID, "data.password")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)

#Confirm Password
    elem_user_email_input = driver.find_element(By.ID, "data.passwordConfirmation")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)
# Sign up button click
    elem_sign_up_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button/span[1]")
    elem_sign_up_login.click()
    print("please Correct email address input.")
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.quit()

#Test Case_5 Verify error message appears for password mismatch
def test_login_with_Enter_Pass_and_Confirm_Pass_differently():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Sign up
    elem_sign_up = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/div[2]/a")
    elem_sign_up.click()
    time.sleep(3)

# Name input
    elem_user_name_input = driver.find_element(By.ID,"data.name")
    elem_user_name_input.clear()
    elem_user_name_input.send_keys("Nadira")
    time.sleep(3)

#Email Address invalidinput
    elem_user_email_input = driver.find_element(By.ID, "data.email")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("nadira.p1999@gmail.com")
    time.sleep(3)

#Password
    elem_user_email_input = driver.find_element(By.ID, "data.password")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)

#Confirm Password
    elem_user_email_input = driver.find_element(By.ID, "data.passwordConfirmation")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345679")
    time.sleep(3)
# Sign up button click
    elem_sign_up_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button/span[1]")
    elem_sign_up_login.click()
    print("Error message should appear: 'The password field must match confirm Password:.'.")
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.quit()
def test_login_with_Enter_already_registered_email():
    driver = webdriver.Chrome()
    driver.get("https://ai-quizwhiz.zluck.com/login")
    driver.maximize_window()

# Sign up
    elem_sign_up = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/div[2]/a")
    elem_sign_up.click()
    time.sleep(3)

# Name input
    elem_user_name_input = driver.find_element(By.ID,"data.name")
    elem_user_name_input.clear()
    elem_user_name_input.send_keys("Nadira")
    time.sleep(3)

#Email Address invalidinput
    elem_user_email_input = driver.find_element(By.ID, "data.email")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("nadira.p1999@gmail.com")
    time.sleep(3)

#Password
    elem_user_email_input = driver.find_element(By.ID, "data.password")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)

#Confirm Password
    elem_user_email_input = driver.find_element(By.ID, "data.passwordConfirmation")
    elem_user_email_input.clear()
    elem_user_email_input.send_keys("12345678")
    time.sleep(3)
# Sign up button click
    elem_sign_up_login = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button/span[1]")
    elem_sign_up_login.click()
    print("Error message should appear:'The email Address: has already been taken.'.")
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.quit()

