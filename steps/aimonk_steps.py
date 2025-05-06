from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
#Homepage(Website opens)
@given('the user launches the AImonk website')
def step_impl(context):
    service = Service(executable_path="/opt/homebrew/bin/chromedriver")  # Path to your ChromeDriver
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get("https://aimonk.com")
    time.sleep(2)

@then('the page title should contain "AIMonk"')
def step_impl(context):
    title = context.driver.title
    assert "AIMonk" in title
    time.sleep(1)

#Technology Feature
@then('the user clicks on the Technology link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Use XPath or class selector instead of link text
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[2]/a")))
    tech_link.click()
    time.sleep(2)  # optional pause to allow navigation

@then('the Technology section should be visible')
def step_impl(context):
    assert "technology" in context.driver.current_url.lower()
    context.driver.quit()

#Use Cases Feature
@then('the user clicks on the Key Use Cases link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Use XPath or class selector instead of link text
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[3]/a")))
    tech_link.click()
    time.sleep(2)  # optional pause to allow navigation

@then('the Key Use Cases section should be visible')
def step_impl(context):
    use_cases_element = context.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/h2")
    assert use_cases_element.is_displayed()

#UnoWho Facial Recognition Feature
@then('the user clicks on the UnoWho Facial Recognition link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Use XPath or class selector instead of link text
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[4]/a")))
    tech_link.click()
    time.sleep(2)  # optional pause to allow navigation

@then('the UnoWho Facial Recognition Engine section should be visible')
def step_impl(context):
    Unowho_Facial_Recognition_Engine_element = context.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div/div/div[2]/h3")
    assert Unowho_Facial_Recognition_Engine_element.is_displayed()

#Blog Feature
@then('the user clicks on the Blog link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Use XPath or class selector instead of link text
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/a")))
    tech_link.click()
    time.sleep(2)  # optional pause to allow navigation

    # Switch to the new tab/window
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])  # assuming the new tab is the second window
    time.sleep(2)
    context.driver.switch_to.window(context.driver.window_handles[0])  # Back to main

#Career
@then('the user clicks on the Career link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Use XPath or class selector instead of link text
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[2]/a")))
    tech_link.click()
    time.sleep(2)  # optional pause to allow navigation

@then('the Career section should be visible')
def step_impl(context):
    assert "career" in context.driver.current_url.lower()
    context.driver.quit()

#Talk to an Expert Button
@then('the user clicks on the Talk to an Expert button')
def step_impl(context):
    expert_button = context.driver.find_element(By.LINK_TEXT, "Talk to an Expert")
    expert_button.click()
    time.sleep(2)  # Give time for the new window to open

