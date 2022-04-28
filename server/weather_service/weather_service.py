from server.main.settings import OPEN_WEATHER_API_KEY
from datetime import datetime
import requests

class WeatherService:
    base_url = "https://api.openweathermap.org/data/2.5/onecall"
    relevant_data_categories = ["clouds", "visibility", "temp", "sunset", "dew_point"]
    timestamp_categories = ["sunset"]

    def __init__(self, location):
        self.location = location
    
    def fetch_weather_data(self):
        payload = {"lat": self.location['lat'],"lon": self.location['lon'], "appid": OPEN_WEATHER_API_KEY, "units": "metric"}
        response = requests.get(self.base_url, params=payload)
        return response.json()
    
    def extract_relevant_data(self, weather_data):
        relevant_data = {}
        relevant_data["current"] = self._extract_current_data(weather_data)
        return relevant_data

    def _extract_current_data(self, weather_data):
        current_relevant_data = {}
        for data_category in self.relevant_data_categories:
            if data_category in self.timestamp_categories:
                current_relevant_data[data_category] = self._convert_time_format(weather_data["current"][data_category])
            else:
                current_relevant_data[data_category] = weather_data["current"][data_category]
            
        return current_relevant_data

    def _convert_time_format(self, timestamp):
        return datetime.fromtimestamp(int(timestamp)).strftime("%d/%m/%Y %H:%M")