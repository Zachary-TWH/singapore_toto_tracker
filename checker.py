import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os
import sys

# ============================================================
# CHANGE THIS VALUE to set your alert threshold (in SGD)
# ============================================================
THRESHOLD = 1_000_000  # notify me when jackpot >= $1,000,000
# ============================================================

def get_jackpot():
    url = "https://www.singaporepools.com.sg/en/product/pages/toto_results.aspx"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    jackpot = soup.select_one(".jackpotAmt").text.strip()
    # Clean "$1,000,000" → 1000000
    cleaned = jackpot.replace("$", "").replace(",", "").strip()
    return int(cleaned), jackpot

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
    sys.exit(1)  # exit code 1 triggers retry in GitHub Actions
