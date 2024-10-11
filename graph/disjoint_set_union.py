# this is ideal for connectivity problems such as detecting cycles and total connections in graph
# the algorithm works by first splitting each node to form a singleton then join them together by using one node as a common parent

class DisjointSet():
    
    def __init__(self, size: int) -> None:
        # convert all nodes to singletons by representing the parent of each element as itself
        self.parent: list[int] = [index + 1 for index in range(size)]
        # default the rank (depth) of each set to 0
        self.rank: list[int] = [0] * size

    def find(self, node: int) -> int:
        """
        Return the immediate group representative (absolute parent) of the current node
        """
        # this uses a recursive approach to find the absolute parent, ensuring that all intermediary nodes parent are set to the original parent of the group
        
        # base case for when the node is the same as its parent
        if node == self.parent[node]:
            return node
        
        # find the immediate parent and assign it to the intermediary nodes in a recursive manner
        subParent = self.find(node)
        self.parent[node] = subParent

        return subParent
    
    def union(self, node1: int, node2: int) -> None:
        """
        Join two sets by
        """
        root1, root2 = self.find(node1), self.find(node2)

        # using the ranks, join the set with lesser rank to the set with higher rank. this will ensure that the new height after the union operation will be max(rank1, rank2)
        rank1, rank2 = self.rank[root1], self.rank[root2]

        # return the edge indicating that they point to the same parent
        

        # after path compression the height changes making the rank represent a pseudo-height
        if rank1 < rank2:
            self.parent[root1] = root2
        elif rank1 > rank2:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
