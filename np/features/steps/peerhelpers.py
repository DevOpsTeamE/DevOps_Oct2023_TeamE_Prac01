from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@then(u'Click "Student Services"')
def step_impl(context):
    dropdown_element = context.driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/div/div/ul/li[5]/button/a")
    actions = ActionChains(context.driver)
    actions.move_to_element(dropdown_element).perform()

@then(u'Click "NP Care Culture"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/header/nav/div[2]/div/div/ul/li[5]/div/div/div/div[2]/div/div[4]/ul/li[4]/a').click()


@then(u'Scroll to Peer Helpers')
def step_impl(context):
    target_element = context.driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")
    context.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    sleep(5)


@then(u'Click on Peer Helpers')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img').click()
    sleep(5)
