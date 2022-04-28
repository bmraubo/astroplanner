from server.main.settings import OPEN_WEATHER_API_KEY
from datetime import datetime
import requests


class WeatherService:
    base_url = "https://api.openweathermap.org/data/2.5/onecall"
    relevant_data_categories = ["clouds", "temp"]

    def __init__(self, location):
        self.location = location

    def fetch_weather_data(self):
        payload = {
            "lat": self.location["lat"],
            "lon": self.location["lon"],
            "appid": OPEN_WEATHER_API_KEY,
            "units": "metric",
        }
        response = requests.get(self.base_url, params=payload)
        return response.json()

    def extract_relevant_data(self, weather_data):
        relevant_data = {}
        relevant_data["current"] = self._extract_current_data(weather_data["current"])
        relevant_data["tonight"] = self._extract_tonight_data(weather_data)
        return relevant_data

    def _extract_current_data(self, current_weather_data):
        current_weather = {}
        current_weather["temp"] = current_weather_data["temp"]
        current_weather["clouds"] = current_weather_data["clouds"]
        current_weather["weather"] = current_weather_data["weather"][0]["main"]
        return current_weather

    def _extract_tonight_data(self, weather_data):
        tonight_relevant_data = {}
        tonight_relevant_data = self._extract_basic_tonight_information(
            weather_data["daily"]
        )
        tonight_relevant_data["hourly"] = self._extract_hourly_tonight_information(
            weather_data["hourly"],
            tonight_relevant_data["sunset"],
            tonight_relevant_data["sunrise"],
        )
        return tonight_relevant_data

    def _extract_basic_tonight_information(self, daily_weather_data):
        tonight_relevant_data = {}
        tonight_relevant_data["sunset"] = self._get_sunset(daily_weather_data[0])
        tonight_relevant_data["sunrise"] = self._get_sunrise(daily_weather_data[1])
        tonight_relevant_data["moonrise"] = daily_weather_data[0]["moonrise"]
        tonight_relevant_data["moonset"] = daily_weather_data[0]["moonset"]
        return tonight_relevant_data

    def _extract_hourly_tonight_information(self, hourly_weather_data, sunset, sunrise):
        hourly_weather = []
        for hour in hourly_weather_data:
            is_nighttime = self._is_after_sunset(
                hour["dt"], sunset
            ) and self._is_before_sunrise(hour["dt"], sunrise)
            if is_nighttime:
                hour_weather = {}
                hour_weather["dt"] = hour["dt"]
                hour_weather["temp"] = hour["temp"]
                hour_weather["clouds"] = hour["clouds"]
                hour_weather["dew_point"] = hour["dew_point"]
                hour_weather["wind_speed"] = hour["wind_speed"]
                hour_weather["precipitation_chance"] = hour["pop"]
                hourly_weather.append(hour_weather)
        return hourly_weather

    def _is_after_sunset(self, timestamp, sunset):
        return timestamp > sunset

    def _is_before_sunrise(self, timestamp, sunrise):
        return timestamp < sunrise

    def _get_sunset(self, today_weather_data):
        return today_weather_data["sunset"]

    def _get_sunrise(self, tomorrow_weather_data):
        return tomorrow_weather_data["sunrise"]

    def _convert_time_format(self, timestamp):
        return datetime.fromtimestamp(int(timestamp)).strftime("%d/%m/%Y %H:%M")
