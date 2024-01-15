def polyEval(poly, x):
    sum = 0

    for i in range(len(poly)):
        sum += poly[i] * pow(x, i)

    return sum


def removeZeroFromEnd(poly):
    endIndex = len(poly) - 1

    if endIndex < 0:
        return poly

    if poly[endIndex] != 0:
        return poly
    else:
        del poly[endIndex]

    return removeZeroFromEnd(poly)


def polySum(poly1, poly2):
    biggerList = poly1 if len(poly1) > len(poly2) else poly2
    sumList = []

    for i in range(len(biggerList)):
        number1 = poly1[i] if i < len(poly1) else 0
        number2 = poly2[i] if i < len(poly2) else 0

        sumList.append(number1 + number2)

    return removeZeroFromEnd(sumList)


def polyMultiply(poly1, poly2):
    result = []

    for i in range(len(poly1)):
        multiplicationResult = [0 for i in range(i)]

        for j in range(len(poly2)):
            multiplicationResult.append(poly1[i] * poly2[j])

        result = polySum(result, multiplicationResult)

    return removeZeroFromEnd(result)
