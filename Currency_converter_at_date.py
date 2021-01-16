import json
import requests
from difflib import get_close_matches



date=input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'): ")
base=input("Convert from (currency) in the format as example: (USD/EUR): ")
curr=input("Convert to (currency) in the format as example: (USD/EUR): ")
base=base.upper()
curr=curr.upper()

base_url="https://api.exchangeratesapi.io/"
url=base_url+date+"?base="+base+"&symbols="+curr

quan=float(input("How much {} do u want to convert:".format(base)))

response=requests.get(url)
if response.ok is False:
    print("\n Error {}:".format(response.status_codes))
    print(response.json()["error"])
else:
    data=response.json()
    rate=data["rates"][curr]
    result=quan*rate
    print("\n{0} {1} is equal to {2} {3},based upon exchanged rates on {4}".format(quan,base,result,curr,data['date']))
    print("Thank you for converting")
