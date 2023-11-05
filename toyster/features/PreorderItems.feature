Feature: Preorder Items
    Background: Common Steps
        Given   Chrome browser is Launched
        When    Open Toyster Preorder page

    Scenario: Add a pre-ordered item to cart
        Then    Add a pre-ordered item
        And     Close browser

    Scenario: Remove a pre-ordered item to cart
        Then    Add and remove pre-ordered item
        And     Close browser

    Scenario: Add multiple pre-ordered item to cart
        Then     Add multiple items
        And     Close browser