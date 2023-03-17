import requests
from twilio.rest import Client

open_weather_map_url = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = 'ea8ab04f1175db01af8cd5cb697154e4'
account_sid = 'AC5049e01b19ee7aecd4cce912bf60ca16'
auth_token = '854589d592083e8db3c27097410ee9e7'


parameters = {
    'lat': 42.874622,
    'lon': 74.569763,
    'appid': api_key,
    'cnt': 5,
    'units': 'metric',
}


response = requests.get(url=open_weather_map_url, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data['list']

will_rain = False

for hour_data in hourly_data:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring the umbrella.",
        from_='+15673648079',
        to='+996704551400'
    )
    print(message.status)