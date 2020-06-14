# app/robo_advisor.py

import requests
import json

#Info Inputs

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
requests.get(request_url)

response = requests.get(request_url)
print(type(response))   #requets.models.Response (data type)
print(response.status_code)  #200
print(response.text)        #string verison of dictionary object

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Deta"]["3. Last Refreshed"]



#breakpoint()

#Info Outputs

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")