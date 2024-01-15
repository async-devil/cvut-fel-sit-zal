class Edge:
    def __init__(self, source: int, target: int, weight: int):
        self.source = source
        self.target = target
        self.weight = weight

class Vertex:
    edges: list[Edge] = []
    previousVertex = None
    minDistance = float("inf")

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class WeightedGraph:
    vertexes: list[Vertex] = []

    def __init__(self, vertexes: list[Vertex], edges: list[Edge]):
        self.vertexes = vertexes

        for vertex in self.vertexes:
            vertex.edges = list(filter(lambda edge: edge.source == vertex.id, edges))

    def findVertex(self, id: int):
        for vertex in self.vertexes:
            if vertex.id == id: return vertex


class PriorityQueue:
    data: list[dict] = []

    def enqueue(self, value: Vertex, priority: int):
        self.data.append({"value": value, "priority": priority})
        self.sort()

    def dequeue(self):
        return self.data.pop(0)

    def sort(self):
        self.data.sort(key=lambda data: data["priority"])

class Dijkstra:
    def createGraph(self, vertexes: list[Vertex], edgesToVertexes: list[Edge]):
        self.weightedGraph = WeightedGraph(vertexes, edgesToVertexes)

    def computePath(self, sourceId: int):
        self.nodes = PriorityQueue()

        for item in self.weightedGraph.vertexes:
            if item.id == sourceId:
                item.minDistance = 0
                self.nodes.enqueue(item, 0)
            else:
                item.minDistance = float("inf")
                self.nodes.enqueue(item, float("inf"))

            item.previousVertex = None

        while(len(self.nodes.data) != 0):
            smallest = self.nodes.dequeue()["value"]
            
            if smallest or smallest.minDistance != float("inf"):
                for edge in smallest.edges:
                    nextNode = self.weightedGraph.findVertex(edge.target)
                    candidate = smallest.minDistance + edge.weight

                    if candidate < nextNode.minDistance:
                        nextNode.minDistance = candidate
                        nextNode.previousVertex = smallest
                        self.nodes.enqueue(nextNode, candidate)

    def getShortestPathTo(self, targetId: int):
        path: list[Vertex] = []

        target = self.weightedGraph.findVertex(targetId)

        while target:
            path.append(target)
            target = target.previousVertex

        path.reverse()

        return path

    def resetDijkstra(self):
        self.nodes = PriorityQueue()

        for vertex in self.weightedGraph.vertexes:
            vertex.minDistance = float("inf")
            vertex.previousVertex = None

    def getVertexes(self):
        return self.weightedGraph.vertexes
