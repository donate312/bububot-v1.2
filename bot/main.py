from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bot.browser import setup_driver
from bot.auth import login
from bot.cart import wait_for_product_and_add_to_cart, proceed_to_checkout, wait_for_cart_update
from bot.autopay import proceed_to_payment
from paypal import paypal_option


def main():

    driver = setup_driver()

    try:
        login(driver)
        wait_for_product_and_add_to_cart(driver)
        wait_for_cart_update(driver)
        proceed_to_checkout(driver)

        if proceed_to_payment(driver):
            try:
                # Updated PayPal logic to handle iframe blocking
                print("[*] Submitting PayPal payment...")

                # Wait for iframe and hide it if needed
                try:
                    iframe = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.component-frame"))
                    )
                    driver.execute_script("arguments[0].style.display = 'none';", iframe)
                    print("[*] Temporarily hid PayPal iframe.")
                except:
                    print("[*] No interfering iframe found.")

                # Scroll and click the Confirm button
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "CONFIRM AND PAY")]'))
                )
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", confirm_button)
                time.sleep(2)
                driver.execute_script("arguments[0].click();", confirm_button)
                print("[+] Submitted PayPal payment.")

            except Exception as e:
                print(f"[!] PayPal automation failed: {e}")

    except Exception as e:
        print(f"[!] An error occurred: {e}")
    finally:
        
        print("[*] Epic Fail.")

if __name__ == "__main__":
    main()

    input("[*] Script finished. Press Enter to close the browser...")
