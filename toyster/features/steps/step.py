from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@given(u'Firefox browser is Launched')
def launchFirefoxBrowser(context):
    context.driver = webdriver.Firefox()

@when(u'Open Toyster page')
def OpenToysterPage(context):
    context.driver.get("https://toyster.sg/")
    context.driver.maximize_window()

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

@then(u'Click GAN option')
def clickChoice(context):
    context.driver.find_element(By.ID,"SortTags").click()
    context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div/header/div[2]/div/div/div[1]/select/option[113]").click()


@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

@then(u'Click the "New Arrival" header button')
def clickNewArrival(context):
    context.driver.implicitly_wait(4)
    context.driver.find_element(By.CSS_SELECTOR,"li.site-nav__item:nth-child(2) > a:nth-child(1)").click()

@then(u'Click a toy and add to cart')
def clickOnToy(context):
    context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div/div[1]/div[8]/a").click()
    context.driver.implicitly_wait(5)

    context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[1]/div/div/div[2]/div/form/div[1]/div/button[2]").click() 
    add_to_cart_element = context.driver.find_element(By.XPATH, "/html/body/div[3]/main/div[1]/div/div/div[2]/div/form/div[2]/button[2]")
    add_to_cart_element.click()
    

@then(u'Checkout cart')
def checkout(context):
    context.driver.implicitly_wait(10)
    cart_element = context.driver.find_element(By.CSS_SELECTOR, "svg.icon.icon-cart")
    context.driver.execute_script("arguments[0].scrollIntoView();", cart_element)
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.icon.icon-cart"))).click()
    context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div/div/div/form/table/tbody/tr/td[2]/p[3]/a").click()
    context.driver.sleep(5)

