Feature: View toy in category
    Scenario: View Toys in G.I. Joe Categories
        Given   Firefox browser is Launched
        When    Open Toyster page
        Then    Verify Toyster Title is present

        And     Click the "Categories" header button
        And     Click "All" in the dropdown list
        Then    Click G.I. Joe option
        And     Close browser

        