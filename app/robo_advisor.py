# app/robo_advisor.py

import requests
import json


def to_usd(my_price):
    return f"${my_price:,.2f}"



#Info Inputs

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
requests.get(request_url)

response = requests.get(request_url)
#print(type(response))   #requets.models.Response (data type)
#print(response.status_code)  #200
#print(response.text)        #string verison of dictionary object

parsed_response = json.loads(response.text)


#dates
dtime = parsed_response["Time Series (Daily)"]
dates = list(dtime.keys())

latest_day = dates[0]  #sort to ensure latest day is first - right now assumes 1st day

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close = dtime[latest_day]["4. close"]


#pricing data
high_prices = []

for date in dates:
    high_price = dtime[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)


low_prices = []

for date in dates:
    low_price = dtime[date]["3. low"]
    low_prices.append(float(low_price))

recent_low = min(low_prices)





#Info Outputs

print("-------------------------")
print("SELECTED SYMBOL: IBM")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")