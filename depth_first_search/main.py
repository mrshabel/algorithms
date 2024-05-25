# from ..data_structures.stack import Stack


def dfs(graph: dict[int, list[int]], start: int) -> dict[int, list[int]]:
    """
    A depth first search algorithm implementation that takes an undirected graph with a starting point and traverse all its adjacent nodes

    Args:
        - graph (dict[int, list[int]]): the graph to be traversed
        - start (int): the start node of the graph

    Returns:
        traversed_graph (dict[int, list[int]]): the output graph as traversed in a depth first search order
    """
    # initialize appropriate data structures to store the visited and adjacent nodes
    visited = []
    adjacent = []

    visited.append(start)
    for i in reversed(graph[start]):
        adjacent.append(i)

    while adjacent:
        current = adjacent.pop()
        if not current in visited:
            visited.append(current)

            for i in reversed(graph[current]):
                if not i in visited:
                    adjacent.append(i)

    return " ".join(map(str, visited))


graph = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [6, 7],
    3: [8, 9],
    4: [10, 11],
    5: [12],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
}

print(dfs(graph, 0))
