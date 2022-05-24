from Temperature import Temperature
from TemperatureScalar import TemperatureScalar


def __TemperatureProcess__(grade1, scale1, grade2, scale2, option):
    v1 = Temperature(grade1, scale1)
    v2 = Temperature(grade2, scale2)

    if option == 1:  # add
        v3 = v1.__add__(v2)
    elif option == 2:  # substract
        v3 = v1.__substract__(v2)
    elif option == 3:  # multiplicativeBy
        v3 = v1.__multiplicateBy__(v2)
    elif option == 4:  # divideBy
        v3 = v1.__divideBy__(v2)
    else:
        return "No Valid"
    return f"(Grade: {v3.grade}, Scalar: {v3.scale})"


if __name__ == '__main__':
    result = __TemperatureProcess__(56, TemperatureScalar.Celsius, 20, TemperatureScalar.Fahrenheit, 1)
    print(result)
