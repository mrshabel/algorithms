from . import AdjacencyList
from collections import deque

def route_between_nodes(graph: AdjacencyList, start: str, end: str) -> bool:
    """
    Given a graph, return True if a route exists between a given start and end nodes
    """
    # an adjacency list will be used in this case with bfs to find the shortest path. 
    # dfs could also be used considering that the solution will be shorter
    if start == end:
        return True
    
    neighbors: deque[str] = deque()
    visited: set[str] = set()

    # add neighbors of start node to the queue
    visited.add(start)

    for node in graph.nodes[start]:
        neighbors.append(node)
    
    # process the nodes level by level

    # take snapshot of current queue length, thus the number of current neighbors
    while neighbors:
        for _ in range(len(neighbors)):
            current = neighbors.popleft()

            # process element only if it has not been visited
            if current not in visited:
                visited.add(current)
                if current == end:
                    return True
                
                # add neighbors
                for neighbor in graph.nodes[current]:
                    neighbors.append(neighbor)
    
    return False

if __name__ == "__main__":
    edges = [["A", "B", "F"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

    graph = AdjacencyList(edges)

    result = route_between_nodes(graph=graph, start="B", end="F")
    print(result)