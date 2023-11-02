Feature: Buy a toy    
    Scenario: Add a toy in shopping cart
        Given   Firefox browser is Launched
        When    Open Toyster page
        Then    Verify Toyster Title is present

        And     Click the "New Arrival" header button
        And     Click a toy and add to cart
        Then    Checkout cart
        And     Close browser
