import unittest

from Kata3 import mainKat3
from Kata3.TemperatureScalarKat3 import TemperatureScalarKat3


class MyTestCase(unittest.TestCase):
    def test_FKMultiplicate(self):
        self.assertEqual((6308.01, 'K'), mainKat3.__TemperatureProcess__(23, TemperatureScalarKat3.Kelvin, 34,
                                                                         TemperatureScalarKat3.Fahrenheit,
                                                                         3))  # Farenheit to Kelvin Multiplicate

    def test_FCDivide(self):
        self.assertEqual((-5.17, 'C'), mainKat3.__TemperatureProcess__(23, TemperatureScalarKat3.Celsius, 24,
                                                                       TemperatureScalarKat3.Fahrenheit,
                                                                       4))  # Farenheit to Celsius Divide

    def test_KCMultiplicate(self):
        self.assertEqual((-4810.45, 'C'), mainKat3.__TemperatureProcess__(23, TemperatureScalarKat3.Celsius, 64,
                                                                          TemperatureScalarKat3.Kelvin,
                                                                          3))  # Kelvin to Celsius Multiplicate

    def test_CFSubstract(self):
        self.assertEqual((-160.4, 'F'), mainKat3.__TemperatureProcess__(12, TemperatureScalarKat3.Fahrenheit, 78,
                                                                        TemperatureScalarKat3.Celsius,
                                                                        2))  # Celsius to Fahrenheit Substract

    def test_FKAdd(self):
        self.assertEqual((372.04, 'K'), mainKat3.__TemperatureProcess__(65, TemperatureScalarKat3.Kelvin, 93,
                                                                        TemperatureScalarKat3.Fahrenheit,
                                                                        1))  # Farenheit to Kelvin add

    def test_FCMultiplicate(self):
        self.assertEqual((137.78, 'C'), mainKat3.__TemperatureProcess__(124, TemperatureScalarKat3.Celsius, 34,
                                                                        TemperatureScalarKat3.Fahrenheit,
                                                                        3))  # Farenheit to Celsius multiplicate

    def test_FCDivide(self):
        self.assertEqual((5.31, 'C'), mainKat3.__TemperatureProcess__(124, TemperatureScalarKat3.Celsius, 74,
                                                                      TemperatureScalarKat3.Fahrenheit,
                                                                      4))  # Farenheit to Celsius divide

    def test_FCNoValid(self):
        self.assertEqual("No valid", mainKat3.__TemperatureProcess__(124, TemperatureScalarKat3.Celsius, 74,
                                                                     TemperatureScalarKat3.Fahrenheit,
                                                                     "jjjf"))  # No Valid


if __name__ == '__main__':
    unittest.main()
