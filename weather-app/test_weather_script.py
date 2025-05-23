import unittest
from unittest.mock import patch
import weather-script as weather_script

class TestWeatherScript(unittest.TestCase):
    @patch('weather-script.requests.get')
    def test_get_weather_success(self, mock_get):
        # Mock a successful API response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 25, "humidity": 40},
            "wind": {"speed": 3.5}
        }
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            weather_script.get_weather("London")
            mock_print.assert_any_call("Weather in London: Clear sky")
            mock_print.assert_any_call("Temperature: 25°C")
            mock_print.assert_any_call("Humidity: 40%")
            mock_print.assert_any_call("Wind speed: 3.5 m/s")

    @patch('weather-script.requests.get')
    def test_get_weather_failure(self, mock_get):
        # Mock a failed API response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            weather_script.get_weather("InvalidCity")
            mock_print.assert_called_with("City not found or API error.")

if __name__ == '__main__':
    unittest.main()