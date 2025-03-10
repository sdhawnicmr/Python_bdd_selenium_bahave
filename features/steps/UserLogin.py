import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'User navigates to Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//span[text()= 'My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)

@when(u'user enters correct username and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("jkdhsfjkh@hjk.com")
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("@Kingfisher6")

@when(u'User clicks on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(2)

@then(u'user should be successfully logged In')
def step_impl(context):
    exp_text = "My Account"
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h2").text.__eq__(exp_text)
    time.sleep(1)
    context.driver.quit()

@when(u'user enters Incorrect username and Valid password')
def step_impl(context):
    #used timestamp
    time_stamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email= "hgdjhgs" +time_stamp+ "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(invalid_email)
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("@Kingfisher6")
    time.sleep(2)

@then(u'user should get message to Enter Invalid password')
def step_impl(context):
    exp_text1 = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH,"//div[contains(text(),"
                                                "'Warning: No match for E-Mail Address and/or Password.')]").text.__eq__(exp_text1)
    time.sleep(1)
    context.driver.quit()

@when(u'user enters correct username and Invalid password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("jkdhsfjkh@hjk.com")
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("@Kingfisher")

@then(u'user should be get message to Enter valid password')
def step_impl(context):
    exp_text2 = "Warning: No match for E-Mail Address and/or Password."
    context.driver.quit()
    context.driver.quit()
    assert (context.driver.find_element(By.XPATH,
                                       "//div[contains(text(), 'Warning: No match for E-Mail Address and/or Password.')]").
    text.__contains__(
        exp_text2))
    time.sleep(1)
    context.driver.quit()