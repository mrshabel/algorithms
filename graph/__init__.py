class GraphNode:
    """
    A graph node is simply the vertex of a graph. This implementation uses adjacency list but there could be other implementations with a regular matrix or an adjacency matrix (square matrix) where the coordinates define the vertexes and the relation between the edges
    """

    def __init__(self, val) -> None:
        self.val = val
        self.neighbors: list[GraphNode] = []

class AdjacencyList:
    """
    An adjacency list containing nodes and their edges
    """
    def __init__(self, edges: list[list[str]]) -> None:
        self.nodes: dict[str, list[str]] = {}

        for current in edges:
            source, destination = current[0], current[1]

            if source not in self.nodes:
                self.nodes[source] = []
            if destination not in self.nodes:
                self.nodes[destination] = []
            
            self.nodes[source].append(destination)