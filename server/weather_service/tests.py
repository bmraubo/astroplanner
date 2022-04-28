from django.test import TestCase
from weather_service.weather_service import WeatherService

# Create your tests here.
class TestWeatherService(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.location = {"lat": 10.00, "lon": 20.00}
        cls.weather_service = WeatherService(cls.location)
        cls.weather_data = cls.weather_service.fetch_weather_data()

    def test_weather_service_can_fetch_weather_data(self):
        self.assertTrue(type(self.weather_data) == dict)
        self.assertTrue("lat" in self.weather_data.keys())
        self.assertEqual(self.weather_data["lat"], self.location["lat"])
        self.assertTrue("lon" in self.weather_data.keys())
        self.assertEqual(self.weather_data["lon"], self.location["lon"])

    def test_weather_service_can_extract_current_relevant_data(self):
        relevant_data = self.weather_service.extract_relevant_data(self.weather_data)
        self.assertTrue(type(relevant_data) == dict)
        self.assertTrue("clouds" in relevant_data["current"].keys())
        self.assertTrue("visibility" in relevant_data["current"].keys())
        self.assertTrue("temp" in relevant_data["current"].keys())
        self.assertTrue("sunset" in relevant_data["current"].keys())
        self.assertTrue("dew_point" in relevant_data["current"].keys())

    def test_weather_service_can_convert_timestamp_to_HH_MM_format(self):
        pass

    