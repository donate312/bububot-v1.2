import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import PRODUCT_URL, MAX_CHECKOUT_RETRIES, CHECKOUT_RETRY_DELAY

def wait_for_product_and_add_to_cart(driver):
    print(f"[*] Navigating to product page: {"PRODUCT_URL"}")
    driver.get("https://www.popmart.com/us/products/86/THE-MONSTERS-Space-Adventures-Series")
    wait = WebDriverWait(driver, 10)

    while True:
        #try:
            add_to_bag_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[5]/div')))
            add_to_bag_button.click()
            print("[+] Added product to bag.")
        #    return
        #except:
        #    print("[-] Product not available yet. Retrying in 15 seconds...")
            time.sleep(15)
        #    driver.refresh()


def proceed_to_checkout(driver):
    print("[*] Navigating to cart page...")
    driver.get("https://popmart.com/us/largeShoppingCart")

    for attempt in range(1, MAX_CHECKOUT_RETRIES + 1):
        try:
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Checkout")]')))
            checkout_button.click()
            print(f"[+] Attempt {attempt}: Proceeded to checkout.")

            # Confirm we're on checkout page (change this selector if needed)
            WebDriverWait(driver, 10).until(
                EC.url_contains("checkout")
            )
            print("[+] Checkout page loaded.")
            return True
        except Exception as e:
            print(f"[-] Attempt {attempt}: Checkout failed. Retrying in {CHECKOUT_RETRY_DELAY}s...")
            time.sleep(CHECKOUT_RETRY_DELAY)
            driver.get("https://popmart.com/us/largeShoppingCart")

    print("[!] Max retries reached. Could not complete checkout.")
    return False
