from behave import given, then  # Remove 'when' if it's not being used
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time

@given('the user launches the AImonk website')
def step_impl(context):
    options = Options()
    options.add_argument('--start-maximized')  # To ensure the window opens maximized
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://aimonk.com")
    time.sleep(2)  # Wait for page to load

@then('the page title should contain "AIMonk"')
def step_impl(context):
    title = context.driver.title
    assert "AIMonk" in title

# Technology Feature
@then('the user clicks on the Technology link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[2]/a")))
    tech_link.click()
    time.sleep(2)

@then('the Technology section should be visible')
def step_impl(context):
    print(f"Current URL: {context.driver.current_url}")
    assert "technology" in context.driver.current_url.lower()

# Use Cases Feature
@then('the user clicks on the Key Use Cases link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[3]/a")))
    tech_link.click()
    time.sleep(2)

@then('the Key Use Cases section should be visible')
def step_impl(context):
    use_cases_element = context.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/h2")
    assert use_cases_element.is_displayed()

# UnoWho Facial Recognition Feature
@then('the user clicks on the UnoWho Facial Recognition link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[4]/a")))
    tech_link.click()
    time.sleep(2)

@then('the UnoWho Facial Recognition Engine section should be visible')
def step_impl(context):
    unowho_facial_recognition_engine_element = context.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div/div/div[2]/h3")
    assert unowho_facial_recognition_engine_element.is_displayed()

# Blog Feature
@then('the user clicks on the Blog link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/a")))
    tech_link.click()
    time.sleep(2)

    # Switch to the new tab/window
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])  # Assuming the new tab is the second window
    time.sleep(2)
    context.driver.switch_to.window(context.driver.window_handles[0])  # Back to main

# Career
@then('the user clicks on the Career link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    tech_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[2]/a")))
    tech_link.click()
    time.sleep(2)

# Talk to an Expert Button
@then('the user clicks on the Talk to an Expert button')
def step_impl(context):
    expert_button = context.driver.find_element(By.LINK_TEXT, "Talk to an Expert")
    expert_button.click()
    time.sleep(2)  # Give time for the new window to open


