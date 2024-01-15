class Car:
    def __init__(
        self, identification: int, name: str, brand: str, price: int, active: bool
    ):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


class Node:
    def __init__(self, nextNode, prevNode, data: Car):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, car: Car) -> Node:
        currentNodePrev = None
        currentNode = self.head

        if self.head is None:
            self.head = Node(None, None, car)
            return

        if car.price < self.head.data.price:
            self.head = Node(self.head, None, car)
            return

        while True:
            if currentNode is None:
                currentNodePrev.nextNode = Node(None, currentNodePrev, car)
                break

            if car.price < currentNode.data.price:
                node = Node(currentNode, currentNodePrev, car)
                currentNode.prevNode = node
                currentNodePrev.nextNode = node
                break

            currentNodePrev = currentNode
            currentNode = currentNode.nextNode

    def find(self, identification: int) -> Node:
        currentNode = self.head

        while currentNode is not None:
            if currentNode.data.identification == identification:
                return currentNode

            currentNode = currentNode.nextNode

        return None

    def print(self) -> None:
        currentNode = self.head

        while currentNode is not None:
            print(
                str(currentNode.data.identification)
                + " "
                + currentNode.data.name
                + " "
                + currentNode.data.brand
                + " "
                + str(currentNode.data.price)
                + " "
                + str(currentNode.data.active)
            )

            currentNode = currentNode.nextNode

    def calculatePrice(self) -> int:
        currentNode = self.head

        total = 0

        while True:
            if currentNode is None:
                break

            if currentNode.data.active:
                total += currentNode.data.price

            currentNode = currentNode.nextNode

        return total


db = LinkedList()


def init(cars: list[Car]):
    for car in cars:
        db.add(car)


def add(car: Car):
    db.add(car)


def updateName(identification: int, name: str) -> Node:
    node = db.find(identification)

    if node is None:
        return node

    node.data.name = name

    return node


def updateBrand(identification: int, brand: str):
    node = db.find(identification)

    if node is None:
        return node

    node.data.brand = brand

    return node


def activateCar(identification: int):
    node = db.find(identification)

    if node is None:
        return node

    node.data.active = True

    return node


def deactivateCar(identification: int):
    node = db.find(identification)

    if node is None:
        return node

    node.data.active = False

    return node


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    return db.calculatePrice()


def clean():
    db.head = None
