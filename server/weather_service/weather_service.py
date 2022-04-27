from server.main.settings import OPEN_WEATHER_API_KEY
import requests

class WeatherService:
    
    def fetch_weather_data(self, location):
        request_url = self.build_request_url(location)
        response = self.make_request(request_url)
        return response.json()

    def build_request_url(self, location):
        return f"https://api.openweathermap.org/data/2.5/onecall?lat={location['lat']}&lon={location['lon']}&exclude=hourly,daily&appid={OPEN_WEATHER_API_KEY}"
    
    def make_request(self, request_url):
        response = requests.get(request_url)
        return response