import time

from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I open Application URL in the Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.magicbricks.com/")
    time.sleep(3)


@when(u'I click signup and enter details')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"normalSignupLink\"]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"ubiusertype1\"]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"ubifname\"]").send_keys("Prince")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"ubiemail\"]").send_keys("sathishsathish36627@gmail.com")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"ubipass\"]").send_keys("Prince@63820")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"ubimobile1\"]").send_keys("6382605974")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"signUp\"]/div/div[10]/div/label").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"signUp\"]/div/div[11]/button").click()
    time.sleep(2)


@then(u'I should get signed up')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)
