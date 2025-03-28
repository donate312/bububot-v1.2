import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# These constants should be defined in config/settings (and imported here)
from config.settings import BAG_URL, MAX_CHECKOUT_RETRIES, CHECKOUT_RETRY_DELAY, PRODUCT_URL

def wait_for_product_and_add_to_cart(driver):
    """
    1. Navigate to the product page
    2. Attempt to click "ADD TO BAG" in a loop until successful
    3. Once added, go to the cart page
    """
    #PRODUCT_URL = "https://www.popmart.com/us/products/86/THE-MONSTERS-Space-Adventures-Series"
    print(f"[*] Navigating to product page: {PRODUCT_URL}")
    driver.get(PRODUCT_URL)

    wait = WebDriverWait(driver, 10)

    while True:
        try:
            add_to_bag_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    '//*[@id="__next"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[5]/div'
                ))
            )
            add_to_bag_button.click()
            print("[+] Added product to bag.")
            break  # Stop looping once the item is added
        except Exception as e:
            print(f"[-] Product not available yet or error occurred: {e}")
            print("[*] Retrying in 15 seconds...")
            time.sleep(15)
            driver.refresh()

def proceed_to_checkout(driver):
    print("[*] Navigating to cart page...")
    driver.get("https://popmart.com/us/largeShoppingCart")
    wait = WebDriverWait(driver, 15)

    for attempt in range(1, MAX_CHECKOUT_RETRIES + 1):
        try:
            print(f"[*] Attempt {attempt}: Waiting for cart to load...")

            # Ensure page is fully loaded
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # Step 1: Wait for and click "Select All" checkbox via JS
            print("[*] Looking for Select All checkbox...")
            select_all = wait.until(EC.presence_of_element_located((
                By.CLASS_NAME, "index_checkbox__w_166"
            )))
            driver.execute_script("arguments[0].click();", select_all)
            print("[+] Selected all items in cart.")
            
            # Step 2: Wait for and click "CHECK OUT" button via JS
            print("[*] Looking for CHECK OUT button...")
            checkout_button = wait.until(EC.presence_of_element_located((
                By.XPATH, '//button[contains(text(), "CHECK OUT")]'
            )))
            driver.execute_script("arguments[0].click();", checkout_button)
            print("[+] Proceeded to checkout.")

            # Step 3: Confirm you're on the checkout page
            wait.until(EC.url_contains("checkout"))
            print("[+] Checkout page loaded.")
            return True

        except Exception as e:
            print(f"[-] Attempt {attempt} failed: {e.__class__.__name__}: {e}")
            driver.save_screenshot(f"checkout_error_attempt{attempt}.png")
            time.sleep(CHECKOUT_RETRY_DELAY)
            driver.get("https://popmart.com/us/largeShoppingCart")

    print("[!] Max retries reached. Could not complete checkout.")
    return False


def select_all_in_cart(driver):
    wait = WebDriverWait(driver, 15)
    """
    Clicks the "Select All" checkbox in the cart.
    Assumes the first checkbox is the "Select All" control.
    """
    for attempt in range(1, MAX_CHECKOUT_RETRIES + 1):
        try:
            # STEP 1: Click "Select All" checkbox using its class
            select_all = wait.until(EC.element_to_be_clickable((
                By.CLASS_NAME, "index_checkbox__w_166"
            )))
            select_all.click()
            print("[+] Selected all items in cart.")
            time.sleep(5)  # Optional: wait a bit to see if it actually checked

            # STEP 2: Click "CHECK OUT" button
            checkout_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//button[contains(text(), "CHECK OUT")]'
            )))
            checkout_button.click()
            print(f"[+] Attempt {attempt}: Proceeded to checkout.")
        # (Optional) Wait a bit to see if it actually checked
            
        except Exception as e:
            print(f"[!] Could not click 'Select All': {e}")
            driver.save_screenshot("select_all_error.png")
            print("[!] Screenshot saved as select_all_error.png for debugging.")
            raise
    
