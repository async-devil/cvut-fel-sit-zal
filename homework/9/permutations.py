def permutations(array: list[int]):
    if len(array) == 0:
        return [[]]

    cache = []

    permute(array, cache)

    return cache


def permute(array: list[int], cache: list[list[int]], shift=0):
    if shift == len(array) - 1:
        return cache.append(array)

    for i in range(shift, len(array)):
        arrayCopy = array[:]
        arrayCopy[shift], arrayCopy[i] = arrayCopy[i], arrayCopy[shift]

        permute(arrayCopy, cache, shift + 1)
