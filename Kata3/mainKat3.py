from Kata3.TemperatureKat3 import TemperatureKat3
from Kata3.TemperatureScalarKat3 import TemperatureScalarKat3

#Method to process the temperature
def __TemperatureProcess__(grade1, scale1, grade2, scale2, option):
    if not grade1 or not scale1 or not grade2 or not scale2 or not option:
        return "Please fill ald fields"
    else:
        v1 = TemperatureKat3(grade1, scale1)
        v2 = TemperatureKat3(grade2, scale2)

        if option == 1:  # add
            v3 = v1.__add__(v2)
        elif option == 2:  # substract
            v3 = v1.__substract__(v2)
        elif option == 3:  # multiplicateBy
            v3 = v1.__multiplicateBy__(v2)
        elif option == 4:  # divideBy
            v3 = v1.__divideBy__(v2)
        else:
            return "No valid"

        return v3

#Main Method
if __name__ == "__main__":
    result = __TemperatureProcess__(12, TemperatureScalarKat3.Celsius, 45, TemperatureScalarKat3.Fahrenheit, 1)
    print(result)
