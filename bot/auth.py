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
    #    driver.save_screenshot("login_error.png")
    #    return  # Exit if login button cannot be clicked
    time.sleep(5)
    
    # Fill in login details and submit
    #try:
    #    # Wait for modal and locate fields
    #    wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "login_modal")]')))
    #    email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    #    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    #    
    #    email_field.send_keys(EMAIL)
    #    password_field.send_keys(PASSWORD)
    #    
    #    # Submit login
    #    submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]')
    #    submit_button.click()
    #    
    #    # Wait for login confirmation by checking for the account element
    #    wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Account")]')))
    #    print("[+] Logged in successfully.")
    #except Exception as e:
    #    print(f"[!] Login failed: {e}")
    #    driver.save_screenshot("login_error.png")
    #    print("[!] Screenshot saved as login_error.png for debugging.")

    
    
