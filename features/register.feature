Feature: Test the functionality of the Register Page

  Background:
    Given I am on the Register Page

  @register
  Scenario: Check that trying to register without completing any field displays error fields
    When I click on the Register button
    Then First name error is displayed
    Then Last name error is displayed
    Then Email error is displayed
    Then Password error is displayed
    Then Confirm password error is displayed

  @register
  Scenario: Check that the registration is successful when completing all the necessary fields
    When I select Female Gender
    When I enter "Ionita" in the First name field
    When I enter "Daniela" in the Last name field
    When I select Day "3" in the Date of birth field
    When I select Month "Iulie" in the Date of birth field
    When I select Year "1997" in the Date of birth field
    When I enter "danielaela037@gmail.com" in the Email field
    When I enter "MyCompany" in the Company name field
    When I uncheck the Newsletter field
    When I insert "ITfactory123" in the Password field
    When I insert "ITfactory123" in the Confirm password field
    When I click on the Register button
    Then The successful registration message is displayed
    Then The successful registration message contains "Your registration completed"
    Then The Continue button is displayed