import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import BAG_URL, MAX_CHECKOUT_RETRIES, CHECKOUT_RETRY_DELAY

MAX_CHECKOUT_RETRIES = 3
CHECKOUT_RETRY_DELAY = 2

def wait_for_product_and_add_to_cart(driver):
    PRODUCT_URL = "https://www.popmart.com/us/products/86/THE-MONSTERS-Space-Adventures-Series"
    print(f"[*] Navigating to product page: {PRODUCT_URL}")
    driver.get(PRODUCT_URL)
    wait = WebDriverWait(driver, 10)

    while True:
        try:
            # Try to find and click the "ADD TO BAG" button
            add_to_bag_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="__next"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[5]/div')
                )
            )
            add_to_bag_button.click()
            print("[+] Added product to bag.")
            
            # Break out of the loop after successful click
            break

        except Exception as e:
            print(f"[-] Product not available yet or error occurred: {e}")
            print("[*] Retrying in 15 seconds...")
            time.sleep(15)
            driver.refresh()  # or driver.get(PRODUCT_URL) if you prefer a full reload

    # After adding the item, go to the cart page
    print("[*] Navigating to cart page...")
    driver.get("https://popmart.com/us/largeShoppingCart")

            

def proceed_to_checkout(driver):
    print("[*] Navigating to cart page...")
    driver.get(BAG_URL)
    
    wait = WebDriverWait(driver, 20)

    for attempt in range(1, MAX_CHECKOUT_RETRIES + 1):
        try:
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Checkout")]')))
            checkout_button.click()
            print(f"[+] Attempt {attempt}: Proceeded to checkout.")

            # Confirm we're on checkout page (change this selector if needed)
            WebDriverWait(driver, 10).until(
                EC.url_contains(lambda d: "checkout" in d.current_url)
            )
            print("[+] Checkout page loaded.")
            return True
        except Exception as e:
            print(f"[-] Attempt {attempt}: Checkout failed. Retrying in {CHECKOUT_RETRY_DELAY}s...")
            time.sleep(CHECKOUT_RETRY_DELAY)
            driver.get("https://popmart.com/us/largeShoppingCart")

    print("[!] Max retries reached. Could not complete checkout.")
    return False

def go_to_cart(driver):
    wait = WebDriverWait(driver, 10)
    try:
        # Wait for the cart icon container to be clickable
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.index_cartItem__xumFD"))
        )
        cart_icon.click()
        print("[+] Clicked the cart icon.")
    except Exception as e:
        print(f"[!] Failed to click the cart icon: {e}")
        driver.save_screenshot("cart_icon_error.png")
        print("[!] Screenshot saved as cart_icon_error.png for debugging.")
        raise
