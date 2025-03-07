from behave import *

@given(u'User navigates to Login page')
def step_impl(context):
    pass

@when(u'user enters correct username and password')
def step_impl(context):
    pass


@when(u'User clicks on Login button')
def step_impl(context):
    pass


@then(u'user should be successfully logged In')
def step_impl(context):
    pass

@when(u'user enters Incorrect username and Valid password')
def step_impl(context):
    pass


@then(u'user should be get message to Enter valid username')
def step_impl(context):
    pass

@when(u'user enters correct username and Invalid password')
def step_impl(context):
    pass

@then(u'user should be get message to Enter valid password')
def step_impl(context):
    pass