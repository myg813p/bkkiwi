import requests
from urllib.parse import quote
from datetime import datetime
import json
import threading

def input_black_kiwi(keywords, params, period):
    def black_kiwi_chart(keyword, params, period, json_combine):

        # endDate
        current_date = datetime.now()
        timestamp = int(current_date.timestamp()) * 1000

        # payload
        params = {
            "keyword": keyword,
            "unit": params,
            "length": period,
            "endDate": timestamp
        }

        # url
        url = "https://blackkiwi.net/api/service/keyword/naver/custom-search-trend"

        # headers
        headers = {
            "Referer": 'https://blackkiwi.net'
        }

        # GET request
        response = requests.get(url, params=params, headers=headers)

        # save
        json_response = response.json()

        # Combine json_response to json_combine
        json_combine[keyword] = json_response

    # Dictionary to store combined json_responses
    json_combine = {}

    # Create threads for each keyword
    threads = []
    for keyword in keywords:
        thread = threading.Thread(target=black_kiwi_chart, args=(keyword, params, period, json_combine))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    with open('통합.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_combine, json_file, indent=4, ensure_ascii=False)

    return json_combine


# List of keywords
keywords = ["슈퍼마리오", "던전앤드래곤", "마이트앤매직", "수박", "포도", '딸기']
params = 'month'
period = '20'


json_combine = input_black_kiwi(keywords, params, period)
print(json_combine)