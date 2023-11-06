from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Chrome browser is launched')
def luanchChromeBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'Open Ngee Ann page')
def openNgeeAnnPage(context):
    context.driver.get("https://www.np.edu.sg/")


@then(u'Verify Ngee Ann is present')
def verifyPageTitle(context):
    title = context.driver.title
    assert title == "Ngee Ann Polytechnic"


@then(u'Click "Full-Time Courses"')
def clickFulltimeCourses(context):
    context.driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div/div/div[1]/ul/li[1]/a").click()


@then(u'Input course title "{courseTitle}"')
def searchCourse(context, courseTitle):
    context.driver.find_element(By.XPATH, '//*[@id="courseListingSearch"]').send_keys(courseTitle)
    context.driver.find_element("id", 'btn-search').click()
    sleep(5)

@then(u'Click "Diploma in Information Technology (IT)"')
def clickCourse(context):
    context.driver.find_element("id", "courseListingData")
    courseLink = context.driver.find_element(By.XPATH, '//*[@id="courseListingData"]/div/div/div')
    courseLink.click()
    sleep(5)



@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()