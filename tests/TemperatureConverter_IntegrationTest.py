import os
import sys
import unittest

# Ensure project root is on sys.path so tests can import `src.*` whether
# they're run from the repository root or from the `tests/` directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.TemperatureConverter import TemperatureConverter

class TestTemperatureConverterIntegration(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()

    def test_round_trip_conversion(self):
        original_celsius = 25
        fahrenheit = self.converter.celsius_to_fahrenheit(original_celsius)
        converted_back = self.converter.fahrenheit_to_celsius(fahrenheit)
        self.assertAlmostEqual(original_celsius, converted_back, places=2)