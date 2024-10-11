def connected_components(n: int, edges: list[tuple[int, int]]) -> int:
    """
    Return the number of connected components that exist in an undirected graph
    """
    count = 0
    # the union find operation will be used to split the edges into singletons and find the common parent, connected component. the distinct number of parents will represent the component count

    # form a singleton for each vertex
    parent = [index for index in range(n)]
    # record their pseudo depth which will be used in determining the sub connected part with lesser height
    rank = [0] * n

    def find(node) -> int:
        # base case for when node is the same as parent
        if node == parent[node]:
            return node
        
        # recursively find the parent and assign it to all intermediate nodes
        subParent = find(parent[node])
        parent[node] = subParent

        return subParent
    

    # define union operation to merge two group representative, parent
    def union(node1: int, node2: int) -> None:
        root1, root2 = find(node1), find(node2)

        # use the ranks to determine how the group will be merged to each other with a common parent
        rank1, rank2 = rank[root1], rank[root2]

        if rank1 < rank2:
            # merge to group 2
            parent[root1] = root2
        elif rank1 > rank2:
            # merge to group 1
            parent[root2] = root1
        else:
            # merge to group 1 and increment rank of group 1 when the ranks are equal
            parent[root2] = root1

            rank[root1] += 1
    
    # perform a union-find on all edges
    for u, v in edges:
        union(u, v)
    
    # return number of distinct parents as the count
    distinctParent = parent[0]
    count += 1
    for val in parent:
        if val != distinctParent:
            count += 1
            distinctParent = val
    
    return count
    

if __name__ == "__main__":
    result = connected_components(n=6, edges=[(0, 1), (1, 2), (3, 4)])
    print(result)