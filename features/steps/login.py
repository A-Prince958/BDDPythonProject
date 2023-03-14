import time

from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I open the Application URL in the Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.magicbricks.com/")
    time.sleep(3)


@given(u'I click the login tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[2]/a").click()
    time.sleep(3)


@when(u'I open the login page')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                 "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[2]/div/div[2]/a").click()
    time.sleep(3)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)
    time.sleep(3)


@when(u'I enter email and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"emailOrMobile\"]").send_keys("prince63820@gmail.com")
    context.driver.find_element(By.XPATH, "//*[@id=\"btnStep1\"]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys("Prince@63820")
    context.driver.find_element(By.XPATH, "//*[@id=\"btnLogin\"]").click()
    time.sleep(5)


@then(u'I should get logged in')
def step_impl(context):
    context.driver.quit()


@when(u'I enter mobile number and otp')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"emailOrMobile\"]").send_keys("6382088426")
    context.driver.find_element(By.XPATH, "//*[@id=\"verifyOtpDiv\"]/div[2]/div[3]/button").click()


@when(u'I click the Google Logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"my-signin2\"]/div/div").click()
    time.sleep(3)


@then(u'I should get navigated to the Google account page')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)

