import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'User navigate to home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)

@when(u'User enters product name in the search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")
    time.sleep(2)

@when(u'clicks on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//div[@id="search"]//button').click()
    time.sleep(2)

@then(u'product should be displayed in the search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    print("Testing first search feature--complete ")
    context.driver.quit()
    time.sleep(2)

@when(u'User enters invalid product name in the search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("jhgashdja")
    time.sleep(2)


@then(u'Message is displayed saying enter the valid product name in the search results')
def step_impl(context):
    expected_text= "There is no product that matches the search criteria."
    assert (context.driver.find_element(By.XPATH, '//input[@id="button-search"]/following-sibling::p')
            .text.__eq__(expected_text))
    context.driver.quit()

@when(u'User do not enters any product in the search box')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert (context.driver.find_element(By.XPATH, '//input[@id="button-search"]/following-sibling::p')
    .text.__eq__(expected_text))
    context.driver.quit()
