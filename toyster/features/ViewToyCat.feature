Feature: View toyster
    Scenario: View Toys in GAN Categories
        Given   Firefox browser is Launched
        When    Open Toyster page
        Then    Verify Toyster Title is present

        And     Click the "Categories" header button
        And     Click "All" in the dropdown list
        Then    Click GAN option
        And     Close browser

    Scenario: Add a toy in shopping cart
        Given   Firefox browser is Launched
        When    Open Toyster page
        Then    Verify Toyster Title is present

        And     Click the "New Arrival" header button
        And     Click a toy and add to cart
        Then    Checkout cart
        And     Close browser


        