from selenium import webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_home_page():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #service = selenium.webdriver.chrome.service.Service("chromedriver.exe")  # update path if needed

    service = selenium.webdriver.chrome.service.Service(executable_path=r"C:\Users\USER\.wdm\drivers\chromedriver\win64\143.0.7499.169\chromedriver-win32\chromedriver.exe")  # update path if needed
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://ai-quizwhiz.zluck.com")
    driver.maximize_window()
    time.sleep(5)
    return driver


def capture_and_print_text(driver):
    wait = WebDriverWait(driver, 15)

    text_element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/main/section[1]/div/div/div[1]/h1/span[1]")
        )
    )

    captured_text = text_element.text
    print("Captured Text:", captured_text)

def main():
    driver = open_home_page()
    capture_and_print_text(driver)
    driver.quit()

if __name__ == "__main__":
    main()
