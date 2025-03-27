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
