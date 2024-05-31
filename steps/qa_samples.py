from behave import given, when, then
from selenium import webdriver
from pages.qa_page import QAPage


@given('I login to the test page')
def launch_browser(context):
    options = webdriver.ChromeOptions()
    mobile_emulation = {
        "deviceName": "iPhone X"
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(
        options=options)
    context.page = QAPage(context.driver)


# Scenario 1
@when('I search for "{query}"')
def search_for_country(context, query):
    context.page.search_for_country(query)


@then('i will see "{query}" selected')
def assert_country(context, query):
    context.page.assert_country(query)


# Scenario 2
@when('I select option 2 from the dropdown')
def select_option(context):
    context.page.select_option(3)


@when('I change the selection to Option 3')
def change_option(context):
    context.page.select_option(4)


@then('I will see Option 3 selected')
def assert_new_option(context):
    context.page.assert_option(3)


# Scenario 3
@when('I open a new window')
def select_option(context):
    context.page.open_new_window()


@then('I assert the "{query}" is present')
def assert_text_present(context, query):
    context.page.switch_window()
    context.page.assert_text_present(query)


# Scenario 4
@when('I open a new tab')
def open_new_tab(context):
    context.page.open_new_tab()


@then('I assert a button')
def assert_button_present(context):
    feature_name = context.feature.name.replace(" ", "_")
    scenario_name = context.scenario.name.replace(" ", "_")
    context.page.switch_window()
    context.page.assert_button_visible(feature_name, scenario_name)


# Scenario 5
@when('I type "QA Card"')
def use_switch_to_alert(context):
    context.page.use_switch_alert("QA Card")


@when('I click the Alert button')
def use_click_to_alert(context):
    context.page.click_alert()


@when('I click the Confirm button')
def use_click_to_alert(context):
    context.page.use_switch_alert("QA Card")
    context.page.click_confirm()


@then('I assert the alert is correct')
def assert_alert(context):
    alert_text = context.page.assert_alert()
    assert alert_text == "Hello QA Card, Are you sure you want to confirm?"


@when('I search for $25, and $15 courses and print them')
def search_for_courses(context):
    context.page.search_for_courses(15, 25)


@when('I search for engineers and businessmans and print their name')
def search_for_courses(context):
    context.page.search_by_prof('Engineer', 'Businessman')


@then('I print them')
def search_for_courses(context):
    pass
