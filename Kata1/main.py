from Temperature import Temperature
from TemperatureScalar import TemperatureScalar


def __TemperatureProcess__(grade1, scale1, grade2, scale2, option):
    v1 = Temperature(grade1, scale1)
    v2 = Temperature(grade2, scale2)

    v3 = v1.__add__(v2)
    return f"(Grade: {v3.grade}, Scalar: {v3.scale})"


if __name__ == '__main__':
    result = __TemperatureProcess__(25, TemperatureScalar.Celsius, 20, TemperatureScalar.Fahrenheit, 1)
    print(result)