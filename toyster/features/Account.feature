Feature: Account
    Background: Common Steps
        Given   Chrome browser is Launched
        When    Open Account page

    Scenario:  Login Account with invalid credentials
        Then    Input with credentials Email "Y" and Password "Y"
        And     Try invalid login
        And     Close browser

    Scenario: Login Account with valid credentials
        Then    Input with credentials Email "d6478481@gmail.com" and Password "Password123!"
        And     Try valid login
        And     Close browser