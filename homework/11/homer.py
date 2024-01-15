"""
Homer's fridge
Course: B0B36ZAL
"""

import copy

# nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name: str, expiration: int):
        self.name = name
        self.expiration = expiration


# predesly kod nijak nemodifikujte!


def openFridge(fridge: list[Food]):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(str(food.name), str(food.expiration)))
    print("")


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""


def maxExpirationDay(fridge: list[Food]):
    if len(fridge) == 0:
        return -1

    maxDay = 0

    for food in fridge:
        maxDay = max(food.expiration, maxDay)

    return maxDay


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""


def histogramOfExpirations(fridge: list[Food]):
    result = [0] * (maxExpirationDay(fridge) + 1)

    for food in fridge:
        result[food.expiration] += 1

    return result


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""


def cumulativeSum(histogram: list[int]):
    result = copy.deepcopy(histogram)

    for i in range(len(result)):
        if i == 0:
            continue

        result[i] += result[i - 1]

    return result


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""


def sortFoodInFridge(fridge: list[Food]):
    sum = cumulativeSum(histogramOfExpirations(fridge))

    result = list(range(len(fridge)))

    for food in fridge:
        sum[food.expiration] -= 1
        result[sum[food.expiration]] = food

    return result


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""


def reverseFridge(fridge: list[Food]):
    fridgeLength = len(fridge)

    result = list(range(fridgeLength))

    for i in range(fridgeLength):
        result[fridgeLength - i - 1] = fridge[i]

    return result


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""


def eatFood(name: str, fridge: list[Food]):
    result = copy.deepcopy(fridge)

    selectedFood = [None] * 2

    for i in range(len(fridge)):
        if fridge[i].name == name:
            if selectedFood[1] is None or selectedFood[1] > fridge[i].expiration:
                selectedFood[0] = i
                selectedFood[1] = fridge[i].expiration

    if selectedFood[0] is not None:
        del result[selectedFood[0]]

    return result


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
