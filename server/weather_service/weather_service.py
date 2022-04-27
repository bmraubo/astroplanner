from server.main.settings import OPEN_WEATHER_API_KEY
import requests

class WeatherService:

    def __init__(self, location):
        self.location = location
        self.request_url = self.build_request_url()
    
    def fetch_weather_data(self):
        response = self.make_request()
        return response.json()

    def build_request_url(self):
        return f"https://api.openweathermap.org/data/2.5/onecall?lat={self.location['lat']}&lon={self.location['lon']}&exclude=hourly,daily&appid={OPEN_WEATHER_API_KEY}"
    
    def make_request(self):
        response = requests.get(self.request_url)
        return response