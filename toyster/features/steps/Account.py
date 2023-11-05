from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from behave import *
from time import sleep

@when(u'Open Account page')
def step_impl(context):
    sleep(1)
    context.driver.find_element(By.ID, 'customer_login_link').click()


@then(u'Input with credentials Email "{email}" and Password "{password}"')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, "CustomerEmail").send_keys(email)
    context.driver.find_element(By.ID, "CustomerPassword").send_keys(password)
    context.driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div/div/div/div[2]/form/p[1]/input').click()

@then(u'Try invalid login')
def step_impl(context):
    assert context.driver.current_url =='https://toyster.sg/account/login'

@then(u'Try valid login')
def step_impl(context):
    assert context.driver.current_url != 'https://toyster.sg/account/login'