import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def paypal_option(driver):
    wait = WebDriverWait(driver, 20)
    print("[*] Submitting PayPal payment...")

    try:
        # Step 1: Wait for the iframe to be present
        iframe = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe.component-frame.visible")
        ))

        # Step 2: Switch to the iframe
        driver.switch_to.frame(iframe)

        # Step 3: Wait for the PayPal button inside iframe (fallback in case needed)
        paypal_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@role="button"]')
        ))
        paypal_button.click()
        print("[+] Submitted PayPal payment.")

        # Step 4: Switch back to default content
        driver.switch_to.default_content()

        # Optional: wait so user can handle login popup manually
        time.sleep(10)

    except Exception as e:
        print(f"[!] PayPal automation failed: {e}")
        driver.switch_to.default_content()

