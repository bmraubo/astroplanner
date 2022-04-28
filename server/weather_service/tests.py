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
        print(relevant_data)

        self.assertTrue(type(relevant_data) == dict)
        self.assertTrue("clouds" in relevant_data["current"].keys())
        self.assertTrue("temp" in relevant_data["current"].keys())
        self.assertTrue("weather" in relevant_data["current"].keys())

    def test_weather_service_can_extract_nighttime_relevant_data(self):
        relevant_data = self.weather_service.extract_relevant_data(self.weather_data)

        self.assertTrue("tonight" in relevant_data.keys())
        self.assertTrue("hourly" in relevant_data["tonight"].keys())

    def test_weather_service_can_extract_correct_information_from_hourly_weather_data(
        self,
    ):
        relevant_data = self.weather_service.extract_relevant_data(self.weather_data)

        self.assertTrue("dt" in relevant_data["tonight"]["hourly"][0])
        self.assertTrue("temp" in relevant_data["tonight"]["hourly"][0])
        self.assertTrue("clouds" in relevant_data["tonight"]["hourly"][0])
        self.assertTrue("dew_point" in relevant_data["tonight"]["hourly"][0])
        self.assertTrue("wind_speed" in relevant_data["tonight"]["hourly"][0])
        self.assertTrue("precipitation_chance" in relevant_data["tonight"]["hourly"][0])

    def test_weather_service_can_extract_hourly_relevant_data_between_sunset_and_sunrise(
        self,
    ):
        relevant_data = self.weather_service.extract_relevant_data(self.weather_data)

        first_hour_timestamp = relevant_data["tonight"]["hourly"][0]["dt"]
        last_hour_timestamp = relevant_data["tonight"]["hourly"][-1]["dt"]
        sunset = relevant_data["tonight"]["sunset"]
        sunrise = relevant_data["tonight"]["sunrise"]
        self.assertTrue(first_hour_timestamp > sunset)
        self.assertTrue(last_hour_timestamp < sunrise)

    def test_weather_service_can_extract_correct_sunrise_and_sunset(self):
        relevant_data = self.weather_service.extract_relevant_data(self.weather_data)

        self.assertTrue("sunset" in relevant_data["tonight"].keys())
        self.assertTrue("sunrise" in relevant_data["tonight"].keys())
        self.assertTrue(
            relevant_data["tonight"]["sunrise"] > relevant_data["tonight"]["sunset"]
        )

    def test_weather_service_can_extract_correct_moonrise_and_moonset(self):
        relevant_data = self.weather_service.extract_relevant_data(self.weather_data)

        self.assertTrue("moonrise" in relevant_data["tonight"].keys())
        self.assertTrue("moonset" in relevant_data["tonight"].keys())
        self.assertTrue(
            relevant_data["tonight"]["moonset"] > relevant_data["tonight"]["moonrise"]
        )

    def test_weather_service_can_convert_timestamp_to_date_time_format(self):
        timestamp = 1618315200
        expected_date_time = "13/04/2021 12:00"

        date_time = self.weather_service._convert_time_format(timestamp)

        self.assertEqual(date_time, expected_date_time)

    # def test_relevant_data_timestamps_have_been_converted(self):
    #     relevant_data = self.weather_service.extract_relevant_data(self.weather_data)

    #     self.assertTrue("/" and ":" in relevant_data["current"]["sunset"])
