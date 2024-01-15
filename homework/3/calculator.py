import math


def addition(x: int, y: int, *args):
    return x + y


def subtraction(x: int, y: int, *args):
    return x - y


def multiplication(x: int, y: int, *args):
    return x * y


def division(x: int, y: int, *args):
    if (y == 0):
        throw()

    return x / y


def modulo(x: int, y: int, *args):
    if (x < y or y <= 0):
        throw()

    return x % y


def secondPower(x: int, *args):
    return pow(x, 2)


def power(x: int, y: int, *args):
    if (y < 0):
        throw()

    return float(pow(x, y))


def secondRadix(x: int, *args):
    if (x <= 0):
        throw()

    return math.sqrt(x)


def magic(x: int, y: int, z: int, k: int):
    l = addition(x, k)
    m = addition(y, z)

    return addition(division(l, m), 1)


def throw():
    raise ValueError(
        "This operation is not supported for given input parameters")


functions = {
    "ADDITION": addition,
    "SUBTRACTION": subtraction,
    "MULTIPLICATION": multiplication,
    "DIVISION": division,
    "MOD": modulo,
    "POWER": power,
    "SECONDRADIX": secondRadix,
    "MAGIC": magic
}


def control(command: str, x: int, y: int, z: int, k: int):
    try:
        function = functions[command]

        return function(x, y, z, k)

    except KeyError:
        throw()
