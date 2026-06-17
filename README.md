# 🎱 TOTO Jackpot Checker

> 有买有希望 

## Why I Built This

Checking TOTO manually is annoying. You forget, you miss it, and before you know it the draw has passed and you never bought a ticket.

But not every jackpot is worth buying. Here's the logic:

- **$1M–$2.5M** — Expected value is already poor at (~$X per dollar spent), and a smaller prize pool only makes it worse. Don't bother.
- **$8M–$12M** — Sounds exciting but no. A big jackpot attracts a flood of buyers, and empirically when the pool exceeds $8M you end up with 4–10 winners splitting it, walking away with roughly $1–2M each anyway.
- **$4M–$5M is the sweet spot.** Big enough to be life-changing. Small enough that you're not splitting it with half of Singapore.

So this bot watches the jackpot daily and only alerts me when it hits the $4M–$5M range.

## How It Works

- Runs automatically at **1pm SGT every day**
- Uses a headless browser to scrape the live jackpot from Singapore Pools
- Jackpot in $4M–$5M range → email alert
- Anything outside that range → silence
- Singapore Pools down for maintenance → script crashes, no email sent (known limitation)
- Once the jackpot qualifies, daily emails continue until someone wins and it resets

---

