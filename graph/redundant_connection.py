def redundant_connection(n: int, edges: list[tuple[int, int]]):
    """
    Return the additional edge that makes the tree cyclic
    """
    # use union-find to spot the additional edge

    parent = [index for index in range(n)]
    rank = [0] * n

    def find(node: int) -> int:
        if node == parent[node]:
            return node
        
        subParent = find(parent[node])
        parent[node] = subParent

        return subParent
    
    def union(node1: int, node2: int) -> bool:
        # find the parents of the nodes
        root1, root2 = find(node1), find(node2)

        if root1 == root2:
            return False
        
        rank1, rank2 = rank[root1], rank[root2]

        if rank1 < rank2:
            parent[root1] = root2
        elif rank1 > rank2:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1
        
        return True
    
    for u, v in edges:
        # if a redundant edge is found
        if not union(u, v):
            return [u, v]
        
    
    return []

if __name__ == "__main__":
    result = redundant_connection(n=4, edges=[(0, 1), (1, 2), (2, 3), (1, 3)])
    print(result)