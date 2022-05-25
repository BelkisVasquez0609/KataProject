import unittest

from Kata3 import MainKt3
from Kata3.TemperatureScaleKt3 import TemperatureScaleKt3


class MyTestCase(unittest.TestCase):
    def test_FCAdd(self):
        self.assertEqual((44.52, 'C'), MainKt3.__TemperatureProcess__(32.3,TemperatureScaleKt3.Celsius,54,TemperatureScaleKt3.Fahrenheit,1)) # Farenheit to Celsius Add

    def test_CKSubstract(self):
        self.assertEqual((-281.85, 'K'), MainKt3.__TemperatureProcess__(34.3,TemperatureScaleKt3.Kelvin,43,TemperatureScaleKt3.Celsius,2)) # Celsius to Kelvin substract

    def test_CFMultiplicate(self):
        self.assertEqual((482.16, 'F'), MainKt3.__TemperatureProcess__(12.3,TemperatureScaleKt3.Fahrenheit,4,TemperatureScaleKt3.Celsius,3)) # Fahrenheit to Celsius MultiplicateBy

    def test_KFDivide(self):
        self.assertEqual((-2.43, 'F'), MainKt3.__TemperatureProcess__(1100.3,TemperatureScaleKt3.Fahrenheit,4,TemperatureScaleKt3.Kelvin,4)) # Kelvin to Fahrenheit Divide

    def test_Nothing(self):
        self.assertEqual('No valid', MainKt3.__TemperatureProcess__(1100.3,TemperatureScaleKt3.Fahrenheit,4,TemperatureScaleKt3.Kelvin,"h")) # Nothing



if __name__ == '__main__':
    unittest.main()