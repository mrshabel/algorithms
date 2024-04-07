"""Shows the path traversed from the start node to the end"""
from collections import deque
def breadth_first_search(nums: dict[str, list[str]], start: str) -> str:
    """ Args: `nums` as a graph containing path and its neighbors"""
    search_queue = deque()
    searched = []
    search_queue += nums[start]

    while search_queue:
        current = search_queue.popleft()
        if not current in searched:
            search_queue += nums[current]
            searched.append(current)

    # convert integers in list to string using map method
    visited_nodes = " ".join(map(str,searched))
    return f"Visited nodes in breadth first search order: {visited_nodes}"

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
    12: []
}


print(breadth_first_search(graph, 0))