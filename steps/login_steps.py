from behave import given, when, then

@given('user is on the login page')
def step_impl(context):
    print("Navigating to login page")

@when('user enters valid username and password')
def step_impl(context):
    print("Entering valid credentials")

@then('user should be redirected to the dashboard')
def step_impl(context):
    print("Redirected to dashboard")
