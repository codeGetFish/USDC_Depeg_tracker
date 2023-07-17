import requests
import time
import winsound

while True:
    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false&precision=ful')
        if response.status_code == 200:
            # Extract the last number from the response
            last_price = response.json()["usd-coin"]["usd"]
            print(last_price)
            
            # Check if the last price is below 1.00 and play sound alert if true
            if last_price < 1.00 and last_price > 0.98:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            elif last_price < 0.98 and last_price > 0.97:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            elif last_price < 0.97 and last_price > 0.96:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            elif last_price < 0.96 and last_price > 0.95:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            elif last_price < 0.94:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

    #Checks every 30 seconds
    time.sleep(30)

