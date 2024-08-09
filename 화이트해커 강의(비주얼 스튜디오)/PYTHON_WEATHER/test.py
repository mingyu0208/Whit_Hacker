import requests

city = input('도시 이름을 입력하세요 : ')
api_key = 'daacd8a9f729a351f1dbe6d1e93d00f3'

url =f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
weather_data = response.json()
print(weather_data)

temp = weather_data['main']['temp']

print(f"현재 온도:{temp}도")