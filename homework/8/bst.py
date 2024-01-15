class Node:
    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    root = None
    visitCount = 0

    def __insert(
        self, value: int, node: Node | None, parent: None | Node = None, isRight=True
    ) -> None:
        if node is None:
            if isRight:
                parent.right = Node(value)
            else:
                parent.left = Node(value)

            return

        if value < node.value:
            return self.__insert(value, node.left, node, False)
        else:
            return self.__insert(value, node.right, node, True)

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        return self.__insert(value, self.root)

    def fromArray(self, array: list[int]) -> None:
        for value in array:
            self.insert(value)

    def __search(self, value: int, node: Node) -> bool:
        if node is None:
            return False

        self.visitCount += 1

        if node.value == value:
            return True

        if value < node.value:
            return self.__search(value, node.left)
        else:
            return self.__search(value, node.right)

    def search(self, value: int) -> bool:
        self.visitCount = 0
        if self.root is None:
            return False

        return self.__search(value, self.root)

    def min(self) -> int:
        if self.root is None:
            return None

        node = self.root
        self.visitCount = 1

        while node.left is not None:
            node = node.left
            self.visitCount += 1

        return node.value

    def max(self) -> int:
        if self.root is None:
            return None

        node = self.root
        self.visitCount = 1

        while node.right is not None:
            node = node.right
            self.visitCount += 1            

        return node.value

    def visitedNodes(self) -> int:
        return self.visitCount
