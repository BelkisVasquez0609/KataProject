from Temperature import Temperature
from TemperatureScalar import TemperatureScalar


def __ConvertionsAndProcess__(grade1, scale1, grade2, scale2, options):
    var1 = Temperature(grade1, scale1)
    var2 = Temperature(grade2, scale2)

    if options == 1:  # add
        var3 = var1.__add1__(var2)
    elif options == 2:  # substract
        var3 = var1.__substractBy__(var2)
    elif options == 3:  # multiplicateBy
        var3 = var1.__multiplicateBy__(var2)
    elif options == 4:  # divideBy
        var3 = var1.__divideBy__(var2)
    else:
        return "No valid"

    return var3


if __name__ == '__main__':
    resultOp = __ConvertionsAndProcess__(25, TemperatureScalar.Celsius, 54, TemperatureScalar.Fahrenheit, 2)
    print(resultOp)
