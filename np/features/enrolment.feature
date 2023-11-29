Feature: View Enrolment guide for PFP students in Ngee Ann Polytechnic's Website
    Scenario: Viewing Enrolment Guide
        Given   Chrome browser launched
        When    Open Ngee Ann Polytechnic's Website
        Then    Click the NP Logo
        Then    Click "Admission & Enrolment"
        Then    Click "Enrolment Guide"
        Then    Click "Your Guide to Enrolling at NP 2023" for PFP students
        And     Close browser