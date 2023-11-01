from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Firefox browser is Launched')
def launchFirefoxBrowser(context):
    context.driver = webdriver.Firefox()

@when(u'Open Toyster page')
def OpenToysterPage(context):
    context.driver.get("https://toyster.sg/")

@then(u'Verify Toyster Title is present')
def verifyPageTitle(context):
    title = context.driver.title
    assert "TOYSTER Singapore" in title


@then(u'Click the "Categories" header button')
def clickCategories(context):
    context.driver.find_element("id","SiteNavLabel-category").click()


@then(u'Click "All" in the dropdown list')
def clickAll(context):
    context.driver.implicitly_wait(3)                                                                                     
    context.driver.find_element(By.XPATH,"/html/body/div[2]/header/div[2]/div/nav/div/div/div[1]/ul/li[3]/div/ul/div/div[1]/li[1]/a").click()

@then(u'Click G.I. Joe option')
def clickChoice(context):
    context.driver.find_element(By.ID,"SortTags").click()
    context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div/header/div[2]/div/div/div[1]/select/option[113]").click()


@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

