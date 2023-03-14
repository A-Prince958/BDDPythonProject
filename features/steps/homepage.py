import time

from behave import given, then, when
from selenium.webdriver.common.by import By


@given(u'I click the search bar')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"keyword_autoSuggestSelectedDiv\"]/div/div[1]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"keyword_autoSuggestSelectedDiv\"]/div/div[2]").click()
    time.sleep(2)


@when(u'I enter the preferred location')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                 "/html/body/section/section/div/div[1]/div[3]/div[1]/div[1]/input").send_keys(
            "Chennai")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"serachSuggest\"]/div[2]/span").click()
    time.sleep(2)


@when(u'I click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                 "//*[@id=\"searchFormHolderSection\"]/section/div/div[1]/div[3]/div[4]").click()
    time.sleep(2)


@then(u'I should get preferred location')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)


@given(u'I click mb prime button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[1]/a").click()
    time.sleep(2)


@when(u'I click join now  button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                 "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[1]/div/div[2]/a").click()
    time.sleep(2)


@then(u'I should get into MB Prime page')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)


@given(u'I click help tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[7]/a").click()
    time.sleep(2)


@when(u'I click help center button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                 "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[7]/div/div/div/ul/li[1]/a").click()
    time.sleep(2)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"userPersonaPopupCloseAnchor\"]").click()
    time.sleep(2)


@when(u'I raise my question and search')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"searchContentInput\"]").send_keys("How to change my mobile number?")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"ui-id-2\"]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"doSearchButton\"]").click()
    time.sleep(2)


@then(u'I should get answers')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)


@given(u'I click buy and rent buttons')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"buyheading\"]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"rentheading\"]").click()
    time.sleep(2)


@when(u'I click sell and home loans buttons')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[3]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[4]/a").click()
    time.sleep(2)


@when(u'I click property and mb advices buttons')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[5]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[6]/a").click()
    time.sleep(2)


@then(u'I should able to open all tabs')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)


@given(u'I scroll down to bottom of the page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


@when(u'I click playstore button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[1]/a").click()
    time.sleep(2)



@when(u'I should get navigate to the play store')
def step_impl(context):
    p = context.driver.window_handles[-1]
    context.driver.switch_to.window(p)
    context.driver.close()
    time.sleep(2)
    q = context.driver.window_handles[0]
    context.driver.switch_to.window(q)
    time.sleep(2)


@when(u'I click app store')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[2]/a").click()
    time.sleep(2)


@then(u'I should get navigate to the app store')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)


@when(u'I click the social media buttons')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[3]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[4]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[5]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[6]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[7]/a").click()
    time.sleep(2)


@then(u'I should get into social media pages')
def step_impl(context):
    context.driver.quit()
    time.sleep(2)
