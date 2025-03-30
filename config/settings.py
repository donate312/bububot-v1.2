import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Core settings
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PRODUCT_URL = os.getenv("PRODUCT_URL")
BAG_URL = os.getenv("BAG_URL")

# Retry settings
MAX_CHECKOUT_RETRIES = 5
CHECKOUT_RETRY_DELAY = 30  # seconds

# Selenium settings
HEADLESS = False  # Set to True to run headless

# PayPal settings
PAYPAL_EMAIL = os.getenv("PAYPAL_EMAIL")
PAYPAL_PASSWORD = os.getenv("PAYPAL_PASSWORD")

# Payment settings
CARD_NUMBER = os.getenv("CARD_NUMBER")
CARD_EXP = os.getenv("CARD_EXP")
CARD_CVV = os.getenv("CARD_CVV")
CARD_NAME = os.getenv("CARD_NAME")

# Shipping settings
SHIPPING_ADDRESS = os.getenv("SHIPPING_ADDRESS")
SHIPPING_CITY = os.getenv("SHIPPING_CITY")
SHIPPING_STATE = os.getenv("SHIPPING_STATE")
SHIPPING_ZIP = os.getenv("SHIPPING_ZIP")