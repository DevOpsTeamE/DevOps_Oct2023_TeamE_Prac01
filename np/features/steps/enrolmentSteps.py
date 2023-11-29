from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@given(u'Chrome browser launched')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'Open Ngee Ann Polytechnic\'s Website')
def step_impl(context):
    context.driver.get("https://www.np.edu.sg/")

@then(u'Click the NP Logo')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/header/nav/div[1]/div/a/img').click()

@then(u'Click "Admission & Enrolment"')
def step_impl(context):
    dropdown_element = context.driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/div/div/ul/li[3]/button/a")
    actions = ActionChains(context.driver)
    actions.move_to_element(dropdown_element).perform()

@then(u'Click "Enrolment Guide"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/header/nav/div[2]/div/div/ul/li[3]/div/div/div/div[2]/div/div[2]/ul/li[1]/a').click()


@then(u'Click "Your Guide to Enrolling at NP 2023" for PFP students')
def step_impl(context):
    target_element = context.driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/div/div[2]/div/div/div/ul/li[1]/a")
    context.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    sleep(5)

