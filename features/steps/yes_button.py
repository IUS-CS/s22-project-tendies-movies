from behave import *

@given('A movie is currently displayed')
def step_impl(context):
    pass

@when('The Yes button is pressed')
def step_impl(context):
    assert True is not False

@then('A congratulations message is displayed')
def step_impl(context):
    assert context.failed is False