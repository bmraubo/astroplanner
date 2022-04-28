from django.test import TestCase
from weather_service.weather_service import WeatherService

# Create your tests here.
class TestWeatherService(TestCase):

    def test_weather_service_can_fetch_weather_data(self):
        location = {"lat": 10.00, "lon": 20.00}
        weather_service = WeatherService(location)
        weather_data = weather_service.fetch_weather_data()
        self.assertTrue(type(weather_data) == dict)
        self.assertTrue("lat" in weather_data.keys())
        self.assertEqual(weather_data["lat"], location["lat"])
        self.assertTrue("lon" in weather_data.keys())
        self.assertEqual(weather_data["lon"], location["lon"])

    def test_weather_service_can_extract_cloud_cover_data(self):
        location = {"lat": 10.00, "lon": 20.00}
        weather_service = WeatherService(location)
        weather_data = weather_service.fetch_weather_data()
        relevant_data = weather_service.extract_relevant_data(weather_data)
        self.assertTrue("clouds" in relevant_data["current"].keys())
        self.assertTrue("visibility" in relevant_data["current"].keys())
        self.assertTrue("temp" in relevant_data["current"].keys())