from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

# Initialize the driver (replace with your chromedriver path if necessary)
driver_path = 'drivers/chromedriver'  # Update this line with the correct path
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be present

def take_screenshot(step_name):
    screenshot_path = f'reports/{step_name}.png'
    driver.save_screenshot(screenshot_path)

@given('I am on the Demo Login Page')
def step_impl(context):
    driver.get("https://www.saucedemo.com/")
    take_screenshot("Demo_Login_Page")

@when('I fill the account information for account {account_type} into the Username field and the Password field')
def step_impl(context, account_type):
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    if account_type == "StandardUser":
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
    elif account_type == "LockedOutUser":
        username_field.send_keys("locked_out_user")
        password_field.send_keys("secret_sauce")
    take_screenshot(f"Fill_Account_Info_{account_type}")

@when('I click the Login Button')
def step_impl(context):
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    take_screenshot("Click_Login_Button")

@then('I am redirected to the Demo Main Page')
def step_impl(context):
    assert "inventory.html" in driver.current_url
    take_screenshot("Redirected_to_Main_Page")

@then('I verify the App Logo exists')
def step_impl(context):
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()
    take_screenshot("Verify_App_Logo")

@then('I verify the Error Message contains the text "{error_message}"')
def step_impl(context, error_message):
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error_message in error.text
    take_screenshot("Verify_Error_Message")

@given('I am on the inventory page')
def step_impl(context):
    driver.get("https://www.saucedemo.com/inventory.html")
    take_screenshot("Inventory_Page")

@when('user sorts products from high price to low price')
def step_impl(context):
    sort_select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_select.select_by_value("hilo")
    take_screenshot("Sort_Products_High_to_Low")

@when('user adds highest priced product')
def step_impl(context):
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    add_to_cart_buttons[0].click()  # Assumes the first button is the highest priced product after sorting
    take_screenshot("Add_Highest_Priced_Product")

@when('user clicks on cart')
def step_impl(context):
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    take_screenshot("Click_Cart")

@when('user clicks on checkout')
def step_impl(context):
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    take_screenshot("Click_Checkout")

@when('user enters first name Alice')
def step_impl(context):
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Alice")
    take_screenshot("Enter_First_Name")

@when('user enters last name Doe')
def step_impl(context):
    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Doe")
    take_screenshot("Enter_Last_Name")

@when('user enters zip code 592')
def step_impl(context):
    zip_code_field = driver.find_element(By.ID, "postal-code")
    zip_code_field.send_keys("592")
    take_screenshot("Enter_Zip_Code")

@when('user clicks Continue button')
def step_impl(context):
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    take_screenshot("Click_Continue")

@then('I verify in Checkout overview page if the total amount for the added item is $49.99')
def step_impl(context):
    total_amount = driver.find_element(By.CLASS_NAME, "summary_total_label")
    assert "$49.99" in total_amount.text
    take_screenshot("Verify_Total_Amount")

@when('user clicks Finish button')
def step_impl(context):
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    take_screenshot("Click_Finish")

@then('Thank You header is shown in Checkout Complete page')
def step_impl(context):
    thank_you_header = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "THANK YOU FOR YOUR ORDER" in thank_you_header.text
    take_screenshot("Verify_Thank_You_Header")
    driver.quit()
