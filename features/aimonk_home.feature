Feature: AImonk homepage

  Scenario: Verify AImonk homepage loads correctly
Given the user launches the AImonk website
Then the page title should contain "AIMonk"

  Scenario: Verify the Technology section
Given the user launches the AImonk website
Then the user clicks on the Technology link
Then the Technology section should be visible

    Scenario: Verify the Use Cases section
      Given the user launches the AImonk website
    Then the user clicks on the Key Use Cases link
    Then the Key Use Cases section should be visible

  Scenario: Verify the UnoWho Facial Recognition section
    Given the user launches the AImonk website
    Then the user clicks on the UnoWho Facial Recognition link
    Then the UnoWho Facial Recognition Engine section should be visible

  Scenario: Verify the Blog link opens in a new window
    Given the user launches the AImonk website
    Then the user clicks on the Blog link

  Scenario: Verify the Career section
    Given the user launches the AImonk website
    Then the user clicks on the Career link


  Scenario: Verify the Talk to an Expert button opens a new window
    Given the user launches the AImonk website
    Then the user clicks on the Talk to an Expert button
