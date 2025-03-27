from bot.browser import setup_driver
from bot.auth import login
from bot.cart import wait_for_product_and_add_to_cart, proceed_to_checkout

def main():
    driver = setup_driver()

    try:
        login(driver)
        wait_for_product_and_add_to_cart(driver)
        proceed_to_checkout(driver)
    except Exception as e:
        print(f"[!] An error occurred: {e}")
    else:
        print("[!] Bot could not complete checkout after multiple attempts.")
    finally:
        driver.quit()
        print("[*] Browser closed.")

if __name__ == "__main__":
    main()
