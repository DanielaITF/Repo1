Feature: Test the functionality of the Cart page

  @cart
  Scenario: Check that the cart is empty
    Given I am on the cart page
    Then The Shopping cart text displayed
    Then The cart page contains the text "Your Shopping Cart is empty!"

  @cart
  Scenario: Check that the "The product has been added to your shopping cart" message is displayed when adding a product to cart
    Given I am on the Jewelry Page
    When I add to cart the "Vintage Style Engagement Ring"
    Then The successful adding to cart message is displayed
    Then The successful message contains "The product has been added to your shopping cart"

  @cart
  Scenario: Check that a product which was added to cart is actually in the cart
    Given I am on the Jewelry Page
    When I add to cart the "Vintage Style Engagement Ring"
    When I click on "Shopping cart" button
    Then I actually am on "https://demo.nopcommerce.com/cart"
    Then The "Vintage Style Engagement Ring" is actually in the cart