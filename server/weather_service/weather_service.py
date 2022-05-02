from server.main.settings import OPEN_WEATHER_API_KEY
import requests

class WeatherService:
    base_url = "https://api.openweathermap.org/data/2.5/onecall"

    def __init__(self, location):
        self.location = location
    
    def fetch_weather_data(self):
        payload = {"lat": self.location['lat'],"lon": self.location['lon'], "appid": OPEN_WEATHER_API_KEY}
        response = requests.get(self.base_url, params=payload)
        return response.json()
    