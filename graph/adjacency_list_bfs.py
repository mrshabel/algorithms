from . import AdjacencyList
from collections import deque

def shortest_path(start: str, target: str, graph: AdjacencyList, ) -> int:
    """
    Find the length of the shortest path to a target node in an adjacency list
    """
    length = 0
    visited: set[str] = set()
    queue: deque[str] = deque()
    
    # process start node
    queue.append(start)
    visited.add(start)

    while queue:
        # take a snapshot of current elements in queue, the neighbors of element in previous iteration
        for _ in range(len(queue)):
            # dequeue the element to be processed
            current = queue.popleft()

            if current == target:
                return length

            # process neighbors of current element
            for neighbor in graph.nodes[current]:
                # only process non-visited nodes
                if not neighbor in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        # increment length after each processing across a breadth
        length += 1
    
    return length


if __name__ == "__main__":
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

    adjacency_list = AdjacencyList(edges)

    result = shortest_path("A", "E", adjacency_list)

    print(result)