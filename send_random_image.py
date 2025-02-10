import requests

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {
    'Authorization':
    f'OAuth {"y0__xDGq61_GJG5GCCtsvWcEh6eJ170OER9T1BO9oLSc9V9wZXl"}'
    }
payload = {'from_date': 1733793600}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
print(homework_statuses.text)

print(homework_statuses.json())
