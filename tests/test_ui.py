from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def test_form_elements_exist():
    driver = get_driver()
    file_path = "file://" + os.path.abspath("index.html")
    driver.get(file_path)

    username_input = driver.find_element(By.ID, "username")
    assert username_input is not None

    password_input = driver.find_element(By.ID, "password")
    assert password_input is not None

    driver.quit()

def test_button_text():
    driver = get_driver()
    file_path = "file://" + os.path.abspath("index.html")
    driver.get(file_path)

    submit_btn = driver.find_element(By.ID, "submitBtn")
    assert submit_btn.text == "Войти"

    driver.quit()

def test_form_input_interaction():
    driver = get_driver()
    file_path = "file://" + os.path.abspath("index.html")
    driver.get(file_path)

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("test_user")
    assert username_input.get_attribute("value") == "test_user"

    driver.quit()
