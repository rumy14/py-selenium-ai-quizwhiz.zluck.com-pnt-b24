from time import sleep

from views.registration.registration import RegistrationPage


URL = "https://ai-quizwhiz.zluck.com/register"



def test_registration_for_checking_confirm_password_valid(driver):
    # Initialize Page Objects
    sign_up_form = RegistrationPage(driver)

    # Open Webpage
    driver.get(URL)


    sign_up_form.enter_name("abcd_004")
    sign_up_form.enter_email("abcd_004@ea.com")
    sign_up_form.enter_password("12345678")
    sign_up_form.enter_confirm_password("12345679")

    sign_up_form.click_sign_up_btn()

    sleep(3)

    sign_up_form.verify_password_corfimation_erorr_message()