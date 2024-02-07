#블랙키위 >> 영향력순위

import requests

url = "https://blackkiwi.net/api/service/statistic/naver/view-tab/author-list"
params = {
    "skip": 0,
    "limit": 100
}

headers = {
    "Referer": "https://blackkiwi.net/service/influence-ranking",
}

response = requests.get(url, headers=headers, params=params)

# Print the response
print(response.status_code)
print(response.text)
