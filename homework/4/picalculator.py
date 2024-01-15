import math


def newtonPi(init):
    prev = 0

    while abs(init - prev) > 0.0000000001:
        prev = init

        init = init - math.sin(init) / math.cos(init)

    return init


def leibnizPi(iterations):
    result = 0

    for i in range(iterations):
        modifier = pow(-1, i)

        result += modifier * 4 / (2 * i + 1)

    return result


def nilakanthaPi(iterations):
    result = 3
    counter = 1

    for i in range(iterations):
        modifier = pow(-1, i+1)

        if i == 0:
            continue

        result += modifier * \
            (4 / ((counter + 1) * (counter + 2) * (counter + 3)))

        counter += 2

    return result
