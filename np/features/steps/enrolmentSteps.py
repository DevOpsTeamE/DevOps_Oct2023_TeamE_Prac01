from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Chrome browser launched')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'Open Ngee Ann Polytechnic\'s Website')
def step_impl(context):
    context.driver.get("https://www.np.edu.sg/")


@then(u'Click "Admission & Enrolment"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="offcanvasNavbarDropdownf190e234-f651-4f9c-819c-2fecfb3c7456"]/a').hover()


@then(u'Click "Enrolment Guide"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[3]/div/div/div/div[2]/div/div[2]/ul/li[1]/a').click()


@then(u'Click "Your Guide to Enrolling at NP 2023" for PFP students')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/main/section[2]/div/div[2]/div/div[2]/div/div/div/ul/li[1]/a').click()
    sleep(5)

