# Method to convert to Farenheit

def __toFarenheit__(grade, scale):
    if scale == "C":
        F = (grade * (9 / 5)) + 32
    elif scale == "K":
        F = (grade - 273.15) * (9 / 5) + 32
    else:
        F = grade
    return F


# Method to convert to Celsius
def __toCelsius__(grade, scale):
    if scale == "F":
        C = (grade - 32) * (5 / 9)
    elif scale == "K":
        C = grade - 273.15
    else:
        C = grade
    return C


# Method to convert to Kelvin
def __toKelvin__(grade, scale):
    if scale == "C":
        K = grade + 273.15
    elif scale == "F":
        K = (grade - 32) * (5 / 9) + 273.15
    else:
        K = grade
    return K


class TemperatureKat3:
    #Constructor
    def __init__(self, Grade, Scale):
        self.grade = Grade
        self.scale = Scale

    # Method to add two temperature
    def __add__(self, other):
        if isinstance(other, TemperatureKat3):
            if self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "F":
                result = __toFarenheit__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"
            return round(self.grade + result, 2), self.scale
        else:
            return "No valid"

    # Method to substract two temperature
    def __substract__(self, other):
        if isinstance(other, TemperatureKat3):
            if self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "F":
                result = __toFarenheit__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"
            return round(self.grade - result, 2), self.scale
        else:
            return "No valid"

    # Method to multiplicateBy two temperature
    def __multiplicateBy__(self, other):
        if isinstance(other, TemperatureKat3):
            if self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "F":
                result = __toFarenheit__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"
            return round(self.grade * result, 2), self.scale
        else:
            return "No valid"

    # Method to divideBy two temperature
    def __divideBy__(self, other):
        if isinstance(other, TemperatureKat3):
            if self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "F":
                result = __toFarenheit__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"
            return round(self.grade / result, 2), self.scale
        else:
            return "No valid"
