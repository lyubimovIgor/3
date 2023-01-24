import requests
import json
from datetime import datetime, timedelta

# Установка дат для поиска
now = datetime.now()
yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
before_yesterday = (now - timedelta(days=2)).strftime("%Y-%m-%d")

# Формирование URL для запроса
url = f"https://api.stackexchange.com/2.2/questions?fromdate={before_yesterday}&todate={yesterday}&tagged=python&site=stackoverflow"

# Отправка запроса
response = requests.get(url)

# Обработка ответа
data = json.loads(response.text)
for item in data["items"]:
    print(item["title"])