import unittest

from Kata1 import main
from TemperatureScalar import TemperatureScalar


class MyTestCase(unittest.TestCase):
    def testFtoCAdd(self):  # fahrenheit to Celsius - add
        self.assertEqual("(Grade: 34.44, Scalar: C)",
                         main.__TemperatureProcess__(30, TemperatureScalar.Celsius, 40, TemperatureScalar.Fahrenheit,
                                                     1))

    def testKtoCAdd(self):  # Kelvin to Celsius - add
        self.assertEqual("(Grade: 339.15, Scalar: K)",
                         main.__TemperatureProcess__(23, TemperatureScalar.Kelvin, 43, TemperatureScalar.Celsius,
                                                     1))

    def testCtoFAdd(self):  # Celsius to Fahrenheit - add
        self.assertEqual("(Grade: 266.6, Scalar: F)",
                         main.__TemperatureProcess__(78, TemperatureScalar.Fahrenheit, 87, TemperatureScalar.Celsius,
                                                     1))

    def testCtoKAdd(self):  # Celsius to Kelvin - add
        self.assertEqual("(Grade: 352.15, Scalar: K)",
                         main.__TemperatureProcess__(23, TemperatureScalar.Kelvin, 56, TemperatureScalar.Celsius,
                                                     1))

    def testKtoCSubstract(self):  # Kelvin to Celsius - Subtract
        self.assertEqual("(Grade: 26.67, Scalar: C)",
                         main.__TemperatureProcess__(45, TemperatureScalar.Celsius, 65, TemperatureScalar.Fahrenheit,
                                                     2))

    def testCtoFSubstract(self):  # Celsius to Fahrenheit - Substract
        self.assertEqual("(Grade: -110.6, Scalar: F)",
                         main.__TemperatureProcess__(78, TemperatureScalar.Fahrenheit, 87, TemperatureScalar.Celsius,
                                                     2))

    def testFtoCSubstract(self):  # Fahrenheit  to Celsius - Substract
        self.assertEqual("(Grade: 27.72, Scalar: C)",
                         main.__TemperatureProcess__(78, TemperatureScalar.Celsius, 122.5, TemperatureScalar.Fahrenheit,
                                                     2))

    def testNoValid(self):  # No Valid
        self.assertEqual("No Valid",
                         main.__TemperatureProcess__(45, TemperatureScalar.Celsius, 65, TemperatureScalar.Fahrenheit,
                                                     "j"))

    def testCtoFMultiplicateBy(self):  # Celsius to Fahrenheit - multiplyBy
        self.assertEqual("(Grade: 2495.6, Scalar: F)",
                         main.__TemperatureProcess__(34, TemperatureScalar.Fahrenheit, 23, TemperatureScalar.Celsius,
                                                     3))

    def testFtoCMultiplicateBy(self):  # Fahrenheit to Celsius - multiplyBy
        self.assertEqual("(Grade: 831.11, Scalar: C)",
                         main.__TemperatureProcess__(34, TemperatureScalar.Celsius, 76, TemperatureScalar.Fahrenheit,
                                                     3))

    def testKtoF(self):  # Kelvin to Fahrenheit - DivideBy
        self.assertEqual("(Grade: -0.26, Scalar: F)",
                         main.__TemperatureProcess__(98, TemperatureScalar.Fahrenheit, 43, TemperatureScalar.Kelvin,
                                                     4))


if __name__ == '__main__':
    unittest.main()
