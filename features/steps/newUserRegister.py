import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'User navigates to Register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//span[text()= 'My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(1)

@when(u'user enters all the fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Japan")
    context.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Kahan")
    context.driver.find_element(By.XPATH, '//input[@id="input-email"]').send_keys("JapanKahan@gmail.com")
    context.driver.find_element(By.XPATH, '//input[@id="input-telephone"]').send_keys("1233211234")
    context.driver.find_element(By.XPATH, '//input[@id="input-password"]').send_keys("@Konhaitumera")
    context.driver.find_element(By.XPATH, '//input[@id="input-confirm"]').send_keys("@Konhaitumera")
    context.driver.find_element(By.XPATH,"//input[@value='0']").click()
    time.sleep(1)
    context.driver.find_element(By.XPATH,"// input[@value='1']").click()

@when(u'User clicks on continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(1)

@then(u'user should be successfully Registered')
def step_impl(context):
    exp_text= "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(exp_text)
    time.sleep(1)
    context.driver.quit()
