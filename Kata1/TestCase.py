import unittest

from Kata1 import main
from TemperatureScalar import TemperatureScalar


class MyTestCase(unittest.TestCase):
    def testFtoC(self):  # fahrenheit to Celsius - add
        self.assertEqual("(Grade: 34.44, Scalar: C)",
                         main.__TemperatureProcess__(30, TemperatureScalar.Celsius, 40, TemperatureScalar.Fahrenheit,
                                                     1))

    def testKtoC(self):  # Kelvin to Celsius - Subtract
        self.assertEqual("(Grade: 26.67, Scalar: C)",
                         main.__TemperatureProcess__(45, TemperatureScalar.Celsius, 65, TemperatureScalar.Fahrenheit,
                                                     2))

    def testCtoF(self):  # Celsius to Fahrenheit - multiplyBy
        self.assertEqual("(Grade: 2495.6, Scalar: F)",
                         main.__TemperatureProcess__(34, TemperatureScalar.Fahrenheit, 23, TemperatureScalar.Celsius,
                                                     3))


if __name__ == '__main__':
    unittest.main()
