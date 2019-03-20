from math import sqrt

# Returns the hypotenuse of a right triangle
def hypoc(a, b):
    return round(sqrt(a**2 + b**2), 2)

def hypoa(b, c):
    return round(sqrt(c**2 - b**2))

def hypob(a, c):
    return round(sqrt(c**2 - a**2))




# Returns the distance between point a and b
def distance(a, b):
    _a = abs(a[0] - b[0])
    b = abs(a[1] - b[1])
    a = _a
    return hypoc(a, b)