Feature: Test Ngee Ann Poly website


    Scenario: View IT course page
        Given Chrome browser is launched
        When Open Ngee Ann page
        Then Click "Full-Time Courses"
        Then Input course title "Information Technology" and search
        #Then Click "Search" button
        Then Click "Diploma in Information Technology (IT)"
        And Close browser


