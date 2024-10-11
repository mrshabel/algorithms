def detect_cycle(n: int, edges: list[tuple[int, int]]):
    """
    Return true if a cycle exists in an undirected graph, else false
    """
    # using the union-find approach

    # split vertices into singleton, parent array, and ranks representing pseudo height of the current parent 
    parent = [index for index in range(n)]
    rank = [0] * n

    # define find operation in a recursive way
    def find(node) -> int:
        # base case for when node is the same as parent
        if node == parent[node]:
            return node
        
        subParent = find(parent[node])
        parent[node] = subParent

        return subParent
    
    # define union operation by merging the edges using the parent singletons
    def union(node1: int, node2: int) -> bool:
        root1, root2 = find(node1), find(node2)

        # a cycle if present if the two nodes point to the same parent
        if root1 == root2:
            return False
        
        # now merge the representative head of the two edges using their head nodes
        rank1, rank2 = rank[root1], rank[root2]

        if rank1 < rank2:
            # merge to parent 2
            rank[root1] = root2
        elif rank1 > rank2:
            # merge to rank 1
            rank[root2] = root1
        else:
            # merge to rank 1 and increment rank 1 count
            rank[root2] = root1
            rank[rank1] += 1
        
        return True
    

    # run the union-find on all the edges provided
    for u, v in edges:
        if not union(u, v):
            return False
    
    return True


if __name__ == "__main__":
    result = detect_cycle(n=5, edges=[(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)])
    print(result)