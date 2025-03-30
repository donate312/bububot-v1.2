from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bot.autopay import proceed_to_payment  # ✅ Make sure this is the correct import path
import time

def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Optional if you want to see browser

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver

if __name__ == "__main__":
    driver = get_driver()

    try:
        print("[*] Opening test checkout page...")
        driver.get("https://popmart.com/us/order-confirmation?source=cart")

        input("[*] Manually log in and click through to make sure you're on the 'Order Confirmation' page. Press Enter when ready...")

        result = proceed_to_payment(driver)
        print("[*] Test result:", "Success ✅" if result else "Failed ❌")

    finally:
        time.sleep(5)
        driver.quit()
