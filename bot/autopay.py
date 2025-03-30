from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def proceed_to_payment(driver):
    wait = WebDriverWait(driver, 15)

    try:
        print("[*] Scrolling to 'PROCEED TO PAY' button...")
        proceed_button = wait.until(EC.presence_of_element_located((
            By.XPATH, '//button[contains(text(), "PROCEED TO PAY")]'
        )))
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", proceed_button)
        time.sleep(5)
        driver.execute_script("arguments[0].click();", proceed_button)
        print("[+] Clicked 'PROCEED TO PAY' button.")
        return True
    except Exception as e:
        print(f"[!] Failed to click 'PROCEED TO PAY': {e}")
        return False


def confirm_pay(driver):
    wait = WebDriverWait(driver, 30)

    try:
        print("[*] Waiting for 'CONFIRM AND PAY' button to appear...")
        wait.until(EC.presence_of_element_located((
            By.XPATH, '//button[contains(text(), "CONFIRM AND PAY")]'
        )))
        print("[*] Payment page detected.")

        print("[*] Refreshing payment page now...")
        driver.refresh()
        time.sleep(6)  # More time to allow full iframe load

        print("[*] Waiting again for 'CONFIRM AND PAY' after refresh...")
        confirm_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, '//button[contains(text(), "CONFIRM AND PAY")]'
        )))

        print("[*] Attempting to click 'CONFIRM AND PAY'...")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", confirm_button)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", confirm_button)

        print("[+] Submitted PayPal payment.")
        time.sleep(7)
        return True

    except Exception as e:
        print(f"[!] PayPal automation failed: {e}")
        return False



#
#def credit_card_option(driver):
#    wait = WebDriverWait(driver, 20)
#    print("[*] Selecting 'Credit Card' payment method...")
#
#    try:
#        # Ensure the whole container is visible first
#        container = wait.until(EC.presence_of_element_located((
#            By.CSS_SELECTOR, ".__next .index_selectContainer__LsrL4"
#        )))
#        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", container)
#        time.sleep(1)
#
#        # Now find the clickable credit card div/span inside the container
#        credit_card_option = wait.until(EC.element_to_be_clickable((
#            By.XPATH, '//div[contains(@class,"index_optionItem") and .//text()[contains(.,"Credit")]]'
#        )))
#        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", credit_card_option)
#        time.sleep(1)
#        driver.execute_script("arguments[0].click();", credit_card_option)
#
#        print("[+] Selected 'Credit Card' option.")
#        return True
#    except Exception as e:
#        print(f"[!] Failed to select credit card option: {e}")
#        return False
#
#def fill_payment_info(driver):
#    wait = WebDriverWait(driver, 20)
#    print("[*] Filling out payment information...")
#
#    try:
#        # Wait for the payment form to load
#        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name^='cardNumber']")))
#
#        # STEP 1: Card Number
#        card_frame = driver.find_element(By.CSS_SELECTOR, "iframe[name^='cardNumber']")
#        driver.switch_to.frame(card_frame)
#        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='encryptedCardNumber']"))).send_keys(os.getenv("CARD_NUMBER"))
#        driver.switch_to.default_content()
#
#        # STEP 2: Expiry
#        exp_frame = driver.find_element(By.CSS_SELECTOR, "iframe[name^='expiryDate']")
#        driver.switch_to.frame(exp_frame)
#        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='encryptedExpiryDate']"))).send_keys(os.getenv("CARD_EXP"))
#        driver.switch_to.default_content()
#
#        # STEP 3: CVV
#        cvv_frame = driver.find_element(By.CSS_SELECTOR, "iframe[name^='securityCode']")
#        driver.switch_to.frame(cvv_frame)
#        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='encryptedSecurityCode']"))).send_keys(os.getenv("CARD_CVV"))
#        driver.switch_to.default_content()
#
#        # STEP 4: Cardholder name
#        name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
#        name_input.send_keys(os.getenv("CARD_NAME"))
#
#        print("[+] Payment form filled.")
#    except Exception as e:
#        print(f"[!] Error filling payment form: {e}")
#    driver.refresh()
#    print("[!] Failed to fill payment information.")
#    return False
#    
#   # Paypal option 
