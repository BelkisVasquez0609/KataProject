from kata3.TemperaatureScalarKata3 import TemperatureScalarKata3
from kata3.TemperatureKata3 import TemperatureKata3


def __TemperaturaOperations__(grade1, scale1, grade2, scale2, option):
    if not grade1:
        return "please fill the required field 'Grade1'"

    if not grade2:
        return "please fill the required field 'Grade2'"

    if not scale1:
        return "please fill the required field 'Scale1'"

    if not scale2:
        return "please fill the required field 'Scale2'"

    if str(grade2).replace('.', ''):
        if str(grade2).isdigit():
            return "please enter a number on the field 'Grade2'"
    if str(grade1).replace('.', ''):
        if str(grade1).isdigit():
            return "please enter a number on the field 'Grade1'"
    if scale1.replace('.', ''):
        if scale1.isnumeric():
            return "please enter a valid text (C,F,K) on the field 'scale1'"
    if scale2.replace('.', ''):
        if scale2.isnumeric():
            return "please enter a valid text (C,F,K) on the field 'scale2'"

    v1 = TemperatureKata3(grade1, scale1)
    v2 = TemperatureKata3(grade2, scale2)

    if option == 1:  # add
        v3 = v1.__add__(v2)
    elif option == 2:  # substract
        v3 = v1.__substractBy__(v2)
    elif option == 3:  # multiplicateBy
        v3 = v1.__multiplicateBy__(v2)
    elif option == 4:  # divideBy
        v3 = v1.__divideBy__(v2)
    else:
        return "No valid"

    return v3


if __name__ == "__main__":
    resultOp = __TemperaturaOperations__(21.3, TemperatureScalarKata3.Celsius, 43.2, TemperatureScalarKata3.Fahrenheit,
                                         1)
    print(resultOp)
