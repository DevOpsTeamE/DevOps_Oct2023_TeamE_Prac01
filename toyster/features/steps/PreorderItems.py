from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from behave import *
from time import sleep

@given(u'Chrome browser is Launched')
def step_impl(context):
    context.driver =webdriver.Chrome()
    context.driver.get("https://toyster.sg/")
    context.driver.maximize_window()


@when(u'Open Toyster Preorder page')
def step_impl(context):
     sleep(1)
     context.driver.find_element(By.CSS_SELECTOR, '#SiteNav > li:nth-child(6) > a').click()


@then(u'Add a pre-ordered item')
def step_impl(context):
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, '#MainContent > div > div.grid.grid--no-gutters.grid--uniform > div:nth-child(1) > a > div.product-card__image-container').click()
    sleep(1)
    itemName =context.driver.find_element(By.CLASS_NAME, "product-single__title").text
    context.driver.find_element(By.CLASS_NAME, "btn.btn--full.btn--secondary-accent.hvr-no.sd_preorder").click()
    sleep(1)
    context.driver.find_element(By.CLASS_NAME, "site-header__cart").click()
    assert context.driver.find_element(By.CLASS_NAME, "h5").text == itemName


@then(u'Add and remove pre-ordered item')
def step_impl(context):
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, '#MainContent > div > div.grid.grid--no-gutters.grid--uniform > div:nth-child(1) > a > div.product-card__image-container').click()
    sleep(1)
    context.driver.find_element(By.CLASS_NAME, "btn.btn--full.btn--secondary-accent.hvr-no.sd_preorder").click()
    sleep(1)
    context.driver.find_element(By.CLASS_NAME, "site-header__cart").click()
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#CartProducts > tr > td:nth-child(2) > p:nth-child(4) > a").click()
    sleep(1)
    try:
        context.driver.find_element(By.CLASS_NAME, 'cart--empty-message')
    except:
        assert 0


@then(u'Add multiple items')
def step_impl(context):
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, '#MainContent > div > div.grid.grid--no-gutters.grid--uniform > div:nth-child(1) > a > div.product-card__image-container').click()
    sleep(1)
    context.driver.find_element(By.CLASS_NAME, 'js-qty__adjust.js-qty__adjust--plus').click()
    context.driver.find_element(By.CLASS_NAME, "btn.btn--full.btn--secondary-accent.hvr-no.sd_preorder").click()
    sleep(1)
    context.driver.find_element(By.CLASS_NAME, "site-header__cart").click()
    sleep(1)
    assert context.driver.find_element(By.CLASS_NAME, "js-qty__input").get_attribute("value") == '2'