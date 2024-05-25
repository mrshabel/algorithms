from collections import deque


def dijkstra(graph: dict[str, dict[str, int]]) -> dict[str, int]:
    """
    Args: `graph`. (a weighted graph)
    returns the shortest distance from the starting node to the each node by using the total cost (sum of weights of edges)
    """
    # define two hash maps (costs and parents)

    # NB: Cost of each node is how long it takes to get to the node from the start

    # infinity = float("inf"). use this when the cost to get to the finish isn't known yet

    # steps: for each current node, select the neighbor with the least cost first. now check the cost from the node with the least cost to its sibling and compare to the cost from the parent to the sibling. update the cost if less
