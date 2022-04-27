from django.test import TestCase
from weather_service.weather_service import WeatherService

# Create your tests here.
class TestWeatherService(TestCase):

    def test_weather_service_can_fetch_weather_data(self):
        weather_service = WeatherService()
        weather_data = weather_service.fetch_weather_data()
        self.assertTrue(type(weather_data) == dict)