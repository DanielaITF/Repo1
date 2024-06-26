from behave import *


@given('I am on the Cart page')
def step_impl(context):
    context.cart_page.navigate_to_cart_page()


@given('I am on the Jewelry Page')
def step_impl(context):
    context.jewelry_page.navigate_to_jewelry_page()


@when('I add to Cart the "Vintage Style Engagement Ring"')
def step_impl(context):
    context.jewelry_page.add_the_vintage_style_engagement_ring_to_cart()


@when('I click on "Shopping cart" button')
def step_impl(context):
    context.cart_page.click_on_shopping_cart_button()


@then('The Shopping cart text displayed')
def step_impl(context):
    assert context.cart_page.is_shopping_cart_text_displayed()


@then('The Cart page contains the text "{empty_text}"')
def step_impl(context, empty_text):
    assert empty_text in context.cart_page.get_cart_empty_text()


@then('The successful adding to Cart message is displayed')
def step_impl(context):
    assert context.jewelry_page.is_successful_added_to_cart()


@then('The successful message contains "{added_product_text}"')
def step_impl(context, added_product_text):
    assert added_product_text in context.jewelry_page.get_successful_added_to_cart_message()


@then('I actually am on "{expected_url}"')
def step_impl(context, expected_url):
    assert context.cart_page.is_url_correct(expected_url)


@then('The "{expected_jewelry}" is actually in the Cart')
def step_impl(context, expected_jewelry):
    assert expected_jewelry in context.cart_page.get_jewelry_name()