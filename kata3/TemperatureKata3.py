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


class TemperatureKata3:
    # Constructor
    def __init__(self, Grade, Scale):
        self.grade = Grade
        self.scale = Scale

    # Add operation
    def __add__(self, other):
        if isinstance(other, TemperatureKata3):
            if self.scale == "F":
                Result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                Result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                Result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.grade = 0
                self.scale = "No Valid"
            return round((self.grade + Result), 2), self.scale  # return the result
        else:
            return "No valid"  # if is not this instance

    # substract operation
    def __substractBy__(self, other):
        if isinstance(other, TemperatureKata3):
            if self.scale == "F":
                Result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                Result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                Result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.grade = 0
                self.scale = "No Valid"
            return round((self.grade - Result), 2), self.scale  # return the result
        else:
            return "No valid"  # if is not this instance

    # multiplicate operation
    def __multiplicateBy__(self, other):
        if isinstance(other, TemperatureKata3):
            if self.scale == "F":
                Result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                Result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                Result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.grade = 0
                self.scale = "No Valid"
            return round((self.grade * Result), 2), self.scale  # return the result
        else:
            return "No valid"  # if is not this instance

    # divide operation
    def __divideBy__(self, other):
        if isinstance(other, TemperatureKata3):
            if self.scale == "F":
                Result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                Result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                Result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.grade = 0
                self.scale = "No Valid"
            return round((self.grade / Result), 2), self.scale  # return the result
        else:
            return "No valid"  # if is not this instance
