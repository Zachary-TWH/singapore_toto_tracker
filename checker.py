import os
import sys
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ============================================================
# CHANGE THIS to set your alert threshold (SGD)
# ============================================================
THRESHOLD = 2_000_000
# ============================================================

def get_jackpot():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.singaporepools.com.sg/en/product/pages/toto_results.aspx")
        wait = WebDriverWait(driver, 20)
        # Wait for jackpot amount to appear
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".jackpot-amount, .jackpotAmt, [class*='jackpot']"))
        )
        text = element.text.strip()
        cleaned = text.replace("$", "").replace(",", "").replace("est", "").strip()
        return int(cleaned), text
    finally:
        driver.quit()

def send_email(jackpot_display):
    msg = MIMEText(f"TOTO Jackpot is now {jackpot_display} — time to buy a ticket!")
    msg["Subject"] = f"TOTO Alert: Jackpot at {jackpot_display}"
    msg["From"] = os.environ["GMAIL_USER"]
    msg["To"] = os.environ["GMAIL_USER"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ["GMAIL_USER"], os.environ["GMAIL_PASS"])
        server.send_message(msg)

try:
    jackpot_value, jackpot_display = get_jackpot()
    print(f"Jackpot: {jackpot_display} | Threshold: ${THRESHOLD:,}")

    if jackpot_value >= THRESHOLD:
        send_email(jackpot_display)
        print("Alert sent.")
    else:
        print("Below threshold. No alert sent.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
