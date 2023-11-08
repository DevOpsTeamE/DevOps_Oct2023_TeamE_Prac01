from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@given(u'Chrome browser is launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open Toyster Page')
def openPage(context):
    context.driver.get("https://toyster.sg/")


@then(u'Verify toyster is present')
def verifyTitle(context):
    title = context.driver.title
    assert "TOYSTER Singapore" in title

@then(u'Click "Age"')
def clickAge(context):
    context.driver.find_element("id", "SiteNavLabel-age").click()
    sleep(2)

@then(u'Click "14 Years and Above"')
def click14years(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div/nav/div/div/div[1]/ul/li[5]/div/ul/div/div/li[6]').click()
    sleep(2)

@then(u'Click "SmartGames - Penguin Parade" game')
def viewGame(context):
    context.driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/div[1]/div[17]/a/div[2]/div[1]').click()
    sleep(2)

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()
