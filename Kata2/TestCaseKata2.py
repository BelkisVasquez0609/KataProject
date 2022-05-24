import unittest

from Kata2 import mainKata2
from TemperatureScalar import TemperatureScalar

class MyTestCase(unittest.TestCase):

    def testNothing(self):
        self.assertEqual("No valid", mainKata2.__ConvertionsAndProcess__(25,TemperatureScalar.Celsius, 54, TemperatureScalar.Fahrenheit, "f"))

    def testCFSubstract(self):
        self.assertEqual((12.78, 'C'), mainKata2.__ConvertionsAndProcess__(25, TemperatureScalar.Celsius, 54,
                                                                         TemperatureScalar.Fahrenheit, 2))
    def testCFmultiplicateBy(self):
        self.assertEqual((305.56, 'C'), mainKata2.__ConvertionsAndProcess__(25, TemperatureScalar.Celsius, 54,
                                                                         TemperatureScalar.Fahrenheit, 3))


if __name__ == '__main__':
    unittest.main()
