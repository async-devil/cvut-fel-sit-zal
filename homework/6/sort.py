def bubbleSort(data: list, compare):
    for i in range(len(data)):
        for j in range(len(data) - (i + 1)):
            cache: int = data[j]

            if (compare(data[j], data[j + 1])):
                data[j] = data[j + 1]
                data[j + 1] = cache

    return data


def getDataFromMappedForm(data: list) -> list[str]:
    parsedData = list()

    for item in data:
        parsedData.append(item[1])

    return parsedData


def sortNumbers(data: list[int], condition: str) -> list[int]:
    if (condition == "ASC"):
        return bubbleSort(data, lambda a, b: a > b)
    if (condition == "DESC"):
        return bubbleSort(data, lambda a, b: a < b)

    raise ValueError("Invalid input data")


def sortData(weights: list[int], data: list[str], condition: str) -> list[str]:
    if (len(weights) != len(data)):
        raise ValueError("Invalid input data")

    mappedData = list()

    for i in range(len(data)):
        mappedData.append([weights[i], data[i]])

    if (condition == "ASC"):
        return getDataFromMappedForm(bubbleSort(mappedData, lambda a, b: a[0] > b[0]))
    if (condition == "DESC"):
        return getDataFromMappedForm(bubbleSort(mappedData, lambda a, b: a[0] < b[0]))

    raise ValueError("Invalid input data")
