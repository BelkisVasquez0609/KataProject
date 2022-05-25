from Kata3.TemperatureScaleKt3 import TemperatureScaleKt3
from Kata3.TemperatureKt3 import TemperatureKt3


def __TemperatureProcess__(grade1, scale1, grade2, scale2, option):
    if not grade1 or not grade2 or not scale1 or not scale2:
        return "Please fill all fields"

    v1 = TemperatureKt3(grade1, scale1)
    v2 = TemperatureKt3(grade2, scale2)

    if option == 1:  # add
        v3 = v1.__add__(v2)
    elif option == 2:  # substract
        v3 = v1.__substractBy__(v2)
    elif option == 3:  # multiplicateBy
        v3 = v1.__multiplicateBy__(v2)
    elif option == 4:  # divideBy
        v3 = v1.__divideBy__(v2)
    else:
        v3 = "No valid"
    return v3


if __name__ == '__main__':
    result = __TemperatureProcess__(12.0, TemperatureScaleKt3.Celsius, 23, TemperatureScaleKt3.Fahrenheit, 1)
    print(result)