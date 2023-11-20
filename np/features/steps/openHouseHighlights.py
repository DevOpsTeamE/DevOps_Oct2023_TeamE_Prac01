from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Chrome browser is launch')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open Ngee Ann Polytechnic\'s Webpage')
def step_impl(context):
    context.driver.get("https://www.np.edu.sg/")


@then(u'Click "Open House Highlights"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/header/nav/div[1]/div/div/div[1]/ul/li[3]/a').click()


@then(u'Click "Find Your Dream Course"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[1]/div[1]/div[1]').click()
    sleep(5)


@then(u'Close google browser')
def closeBrowser(context):
    context.driver.close()