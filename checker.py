import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=options)
try:
    driver.get("https://www.singaporepools.com.sg/en/product/pages/toto_results.aspx")
    
    # Wait for JS to fully render the page
    time.sleep(10)
    
    # Search for anything containing "2,500" or "Jackpot"
    elements = driver.find_elements(By.XPATH, "//*[contains(text(), '2,500') or contains(text(), 'Jackpot') or contains(text(), 'jackpot')]")
    for el in elements:
        print("TAG:", el.tag_name)
        print("CLASS:", el.get_attribute("class"))
        print("TEXT:", repr(el.text[:200]))
        print("---")
finally:
    driver.quit()
