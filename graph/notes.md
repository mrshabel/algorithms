# Graphs

### Disjoint Sets

The operations involved in a disjoint set are _find_ and _union,_ commonly referred to as the find-union operation. This helps in cycle detection and determining how edges are connected in a graph.

-   **Find**: this operation ensures that the group to which a node belongs is found and returned. A representative which acts as a common parent is chosen for all nodes in a particular group
-   **Union**: in this operation, two sets are combined where the one with lesser rank (depth) is merged to the other with higher rank to become its child. This helps in maintaining balance in the height of the tree

Union by Rank and Path Compression are optimization techniques to reduce the number of operations. Path compression ensures that the immediate parents of nodes in a sub-group are replaced by the original parent of the entire group after merging, thus, making parent finding a constant time operation.

### Multisource BFS Traversal

This involves a bfs traversal where there are more than 1 starting point as compared to the traditional traversal means which starts from a single source. The starting points are first enqueued even before the bfs starts. The FIFO property of a queue then allows processing of the elements in an order relative to each starting point level by level. If the problem involves calculating the path along each level, a snapshot of the initial queue length can be taken where the distance is incremented after each level. This ensures that distances relative to the starting points are effectively measured

.
