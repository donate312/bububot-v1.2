from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import EMAIL, PASSWORD

import time

def accept_policy(driver):
    wait = WebDriverWait(driver, 5)
    try:
        accept_div = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "policy_acceptBtn__ZNU71"))
        )
        accept_div.click()
        print("[+] Accepted cookie/policy popup.")
    except Exception:
        print("[*] No policy popup found or already accepted.")

def login(driver):
    print("[*] Navigating to home page...")
    driver.get("https://popmart.com/us/user/login")
    wait = WebDriverWait(driver, 20)
    
    # Handle cookie popup
    accept_policy(driver)


    email_field = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '//input[@placeholder="Enter your e-mail address"]')
    )
)
    email_field.send_keys(EMAIL)
        
    continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "CONTINUE")]'))
        )
    continue_button.click()
    print("[*] Clicked the CONTINUE button.")

    password_field = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter your password"]'))
)
    password_field.send_keys(PASSWORD)
    # Attempt to click the "SIGN IN" button
    try:
        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(translate(text(), "SIGNIN", "signin"), "sign in")]')
            )
        )
        login_button.click()
    except Exception as e:
        print(f"[!] Error clicking the login button: {e}")
    time.sleep(5)
    
    
    
