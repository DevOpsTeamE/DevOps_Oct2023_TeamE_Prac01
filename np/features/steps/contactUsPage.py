from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Chrome browser launch')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open Ngee Ann Webpage')
def step_impl(context):
    context.driver.get("https://www.np.edu.sg/")


@then(u'Click "Back to NP Home"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/header/nav/div[1]/div/div/div[1]/ul/li[5]/a').click()
    sleep(3)


@then(u'Click "Contact Us"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/header/nav/div[1]/div/div/div[1]/ul/li[5]/a').click()
    sleep(3)


@then(u'Close chrome browser')
def closeBrowser(context):
    context.driver.close()
