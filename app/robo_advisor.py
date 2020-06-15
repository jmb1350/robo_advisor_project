# app/robo_advisor.py

import json
import csv
import os
import datetime

from dotenv import load_dotenv
import requests

load_dotenv()


def to_usd(my_price):
    return f"${my_price:,.2f}"



#Info Inputs and Data Requests
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
symbol = input("Please input a ticker symbol:")


while symbol.isdigit():
    symbol = input("Sorry, I couldn't understand that symbol. Please try again: ")
   #https://www.w3schools.com/python/ref_string_isdigit.asp
   #filtered out digits from ticker without len function, since tickers can be a single letter


request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

requests.get(request_url)

response = requests.get(request_url)

parsed_response = json.loads(response.text) 

if "Error" in response.text:   
        print("Sorry, data isn't available. Please try again later.") 
        exit()







#DATES

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]  

latest_close = tsd[latest_day]["4. close"]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]






#PRICING DATA
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)











#WRITING TO CSV

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above 
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"], 
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume":daily_prices["5. volume"]
        })











#INFO OUTPUTS

print("-------------------------")
print("SELECTED SYMBOL: " + symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")

high_multiple = float(recent_high) * .2
close_formula = float(high_multiple) + float(latest_close)

#https://www.journaldev.com/23715/python-convert-string-to-float#:~:text=We%20can%20convert%20a%20string,object%20__float__()%20function.
#used the above webite to realize that everything had to be converted to float for the calculations

print("-------------------------")

if float(close_formula) <= float(recent_high):
    print("RECOMMENDATION: Buy! This stock is a good deal!")
else:
    print("RECOMMENDATION: Don't buy! This stock is too expensive.")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")





#print("Sorry, data isn't available. Please try again later.")    