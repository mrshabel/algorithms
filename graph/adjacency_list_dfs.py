from . import AdjacencyList
def paths_in_adjacency_list(start: str, target: str, graph: AdjacencyList) -> int:
    """
    Count paths from a start node to target in an adjacency list
    """

    def dfs(node: str, target: str, graph: AdjacencyList, visited: set[str]) -> int:
        # base case
        if node in visited:
            return 0
        
        if node == target:
            return 1

        # recursive step
        count = 0

        # mark current node as visited
        visited.add(node)

        # visit all neighbors of node and their child nodes recursively
        for neighbor in graph.nodes[node]:
            count += dfs(node=neighbor, target=target, graph=graph, visited=visited)
        
        visited.remove(node)
        
        return count
    
    return dfs(start, target, graph, set())


if __name__ == "__main__":
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

    adjacency_list = AdjacencyList(edges)

    result = paths_in_adjacency_list("A", "E", adjacency_list)

    print(result)