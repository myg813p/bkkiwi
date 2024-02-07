import requests
from urllib.parse import quote
from datetime import datetime
import json

#keyword
keyword = "떡참"
encoded_keyword = quote(keyword, safe='')

#endDate
current_date = datetime.now()
timestamp = int(current_date.timestamp()) * 1000

# payload
params_year = {
    "keyword": keyword,
    "unit": "year",
    "length": "5",
    "endDate": timestamp
}
params_month = {
    "keyword": keyword,
    "unit": "month",
    "length": "20",
    "endDate": timestamp
}
params_date = {
    "keyword": keyword,
    "unit": "date",
    "length": "31",
    "endDate": timestamp
}

#url
url = "https://blackkiwi.net/api/service/keyword/naver/custom-search-trend"

#headers
headers = {
    "Referer": f"https://blackkiwi.net/service/keyword-analysis?keyword={encoded_keyword}&platform=naver",
}

#GET request
response = requests.get(url, params=params_month, headers=headers)

#save
json_response = response.json()
with open(f'{keyword}.json', 'w') as json_file:
    json.dump(json_response, json_file, indent=4)
