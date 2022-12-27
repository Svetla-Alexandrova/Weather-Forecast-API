import requests

def get_forecast(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open('data.txt', 'a') as file:
    for dict_item in content['list']:
      file.write(f"{dict_item['dt_txt']}, {dict_item['main']['temp']}, {dict_item['weather'][0]['description']}\n")
      
  return content

print(get_forecast(city='Sofia'))