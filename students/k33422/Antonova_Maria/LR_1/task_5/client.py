# альтернативный вариант
import requests

data = {'subject': 'Лин алгебра', 'grade': '5'}
response = requests.post('http://localhost:8080/', data=data)
print(response)