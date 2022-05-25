# Method to convert to Fahrenheit
def __toFahrenheit__(grade, scale):
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
        C = (grade - 273.15)
    else:
        C = grade
    return C


# Method to convert to Kelvin
def __toKelvin__(grade, scale):
    if scale == "C":
        K = (grade + 273.15)
    elif scale == "F":
        K = (grade - 32) * (5 / 9) + 273.15
    else:
        K = grade
    return K


class TemperatureKt3:
    # constructor
    def __init__(self, Grade, Scale):
        self.grade = Grade
        self.scale = Scale

    def __add__(self, other):
        if isinstance(other, TemperatureKt3):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"

            return round(self.grade + result, 2), self.scale
        else:
            return "No valid"

    def __substractBy__(self, other):
        if isinstance(other, TemperatureKt3):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"

            return round(self.grade - result, 2), self.scale
        else:
            return "No valid"

    def __multiplicateBy__(self, other):
        if isinstance(other, TemperatureKt3):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"

            return round(self.grade * result, 2), self.scale
        else:
            return "No valid"

    def __divideBy__(self, other):
        if isinstance(other, TemperatureKt3):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                return "No valid"

            return round(self.grade / result, 2), self.scale
        else:
            return "No valid"
