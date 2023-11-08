Feature: Test Toyster Website
    Scenario: View a game for people above 14
        Given Chrome browser is launched
        When Open Toyster Page
        Then Verify toyster is present
        Then Click "Age"
        Then Click "14 Years and Above"
        Then Click "SmartGames - Penguin Parade" game
        And Close browser
