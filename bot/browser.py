import undetected_chromedriver as uc
from config.settings import HEADLESS

def setup_driver():
    options = uc.ChromeOptions()
    
    if HEADLESS:
        options.add_argument("--headless")
        
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    print("[*] Launching browser...")
    driver = uc.Chrome(options=options)
    return driver
