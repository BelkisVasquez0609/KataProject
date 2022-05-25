import unittest

from kata3 import mainKata3
from kata3.TemperaatureScalarKata3 import TemperatureScalarKata3


class MyTestCase(unittest.TestCase):

    def test_FCAdd(self):
        self.assertEqual((29.11, 'C'), mainKata3.__TemperaturaOperations__(23.0, TemperatureScalarKata3.Celsius, 43.0,
                                                                           TemperatureScalarKata3.Fahrenheit,
                                                                           1))  # Celsius to Fahrenheit add

    def test_KCSubstract(self):
        self.assertEqual((265.15, 'C'), mainKata3.__TemperaturaOperations__(15.0, TemperatureScalarKata3.Celsius, 23.0,
                                                                            TemperatureScalarKata3.Kelvin,
                                                                            2))  # Kelvin to Celsius substract

    def test_CFMultiplicate(self):
        self.assertEqual((3963.6, 'F'),
                         mainKata3.__TemperaturaOperations__(54.0, TemperatureScalarKata3.Fahrenheit, 23.0,
                                                             TemperatureScalarKata3.Celsius,
                                                             3))  # Celsius to Fahrenheit multiplicate

    def test_FKDivide(self):
        self.assertEqual((0.20, 'K'), mainKata3.__TemperaturaOperations__(54.0, TemperatureScalarKata3.Kelvin, 23.0,
                                                                          TemperatureScalarKata3.Fahrenheit,
                                                                          4))  # Fahrenheit to Kelvin Divide

    def test_FCsubstract(self):
        self.assertEqual((-1844.92, 'C'),
                         mainKata3.__TemperaturaOperations__(45.3, TemperatureScalarKata3.Celsius, 3434.4,
                                                             TemperatureScalarKata3.Fahrenheit,
                                                             2))  # Fahrenheit to Celsius substract

    def test_KCAdd(self):
        self.assertEqual((3392.55, 'C'),
                         mainKata3.__TemperaturaOperations__(3453.3, TemperatureScalarKata3.Celsius, 212.4,
                                                             TemperatureScalarKata3.Kelvin,
                                                             1))  # Kelvin to Celsius add

    def test_CFDivide(self):
        self.assertEqual((8.33, 'F'),
                         mainKata3.__TemperaturaOperations__(3453.3, TemperatureScalarKata3.Fahrenheit, 212.4,
                                                             TemperatureScalarKata3.Celsius,
                                                             4))  # Celsius to Farenheit divide

    def test_FKMultiplicate(self):
        self.assertEqual((1289366.29, 'K'),
                         mainKata3.__TemperaturaOperations__(3453.3, TemperatureScalarKata3.Kelvin, 212.4,
                                                             TemperatureScalarKata3.Fahrenheit,
                                                             3))  # Farenheit to Kelvin multiplicate

    def test_FKNothing(self):
        self.assertEqual("No valid", mainKata3.__TemperaturaOperations__(3453.3, TemperatureScalarKata3.Kelvin, 212.4,
                                                                         TemperatureScalarKata3.Fahrenheit,
                                                                         "f"))  # Nothing -> No Valid

    def test_FKAdd(self):
        self.assertEqual((307.67, 'K'), mainKata3.__TemperaturaOperations__(34.3, TemperatureScalarKata3.Kelvin, 32.4,
                                                                            TemperatureScalarKata3.Fahrenheit,
                                                                            1))  # Fahrenheit to Kelvin Add


if __name__ == '__main__':
    unittest.main()
