import unittest

class TestTemperatureConverterUnit(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(212), 100)