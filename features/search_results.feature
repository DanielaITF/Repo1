Feature: Test the functionality of the Search input

  Background:
    Given I am on the Home Page

  @search_results
  Scenario: Check that the user can use the search functionality - without examples table
    When I type "Shirt" in the search input
    When I click the search button
    Then Search results are displayed
    Then All the search results contain the word "Shirt"

  @search_results
  Scenario Outline: Check that the user can use the search functionality - with examples table
    When I type "<text>" in the search input
    When I click the search button
    Then Search results are displayed
    Then All the search results contain the word "<text>"
    Examples:
      | text |
      | laptop |
      | phone |
      | shirt |
      | camera |