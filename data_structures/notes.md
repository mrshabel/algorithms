# Data Structures

## Hashmap

This implementation uses an array under the hood where the values stored are the entries of the hashmap (key, value). The insertion mechanism uses a mathematical modulus approach which ensures that no entry goes out of bounds. The elements are added in such a way that looks as if they were in a circle.

Two keys with the same hash will collide hence the need for a collision resolution. Resizing the internal array when full can result lead to potential errors when retrieving previously saved values and hence the need to **rehash** the contents again.

Rehashing is done when the hashmap is halfway full and since this is an infrequent action, the complexity is still negligible an considered as a constant time operation ( **Amortized time** ).

From a mathematical perspective, the size of the array should be a prime number to reduce collisions. Whenever the size is doubled and the result isn't a prime number, the closest prime number to that result is then used as the new size. The property of a prime number which restricts it from having any other factors aside itself and 1 helps reduce the possibly of the modulus of hashcodes being the same.

#### Collision Resolution of Hashmap

-   **Chaining**: This involves using linked lists to hold the key and value of a hashmap entry at every index of the array rather than storing the entries themselves. In this way, two or more keys with the same hashes goes into the same linked list where a traversal needs to be performed in order to find the needed element. The downside to this approach is that additional memory space is required to hold the linked list and its' pointers.
-   **Open Addressing**: Indexes are loosely tied to the hash in this approach where in the case of a collision, the entry is moved to the next available address. A downside to this is that in the event of many collisions, the values can be clustered around a particular value especially when using a regular incremental approach to find the next available address.

---

## Heap

The heap data structure uses a priority queue interface, hence the name **heap / priority queue**. Max and min heap are the common implementations of a heap data structure. For a min-heap, every descendant of a node should be greater than or equal to the node. The two properties of a binary heap under consideration are:

-   Structure property: The binary heap is simply a complete binary tree, every single level in the tree is completely full except possibly the last level which is balanced at the left. Nodes are added in level-order to maintain the completeness of the tree.
-   Order property: For a min-heap, the minimum value among all nodes should be at the root. Duplicates are allowed in the heap.

The elements to be added to a priority queue are mostly kept in arrays where the 0 index holds nothing. The root is kept at index 1 with its children being stored in the array from left to right. The maths behind this is:

```
left child: 2 * i
right child 2 * i + 1
parent i / 2, where i is the index of the array
```

This gives a fair idea of where the parents and children of the elements are placed. To find the parent from the right child (odd index), the result of `i / 2` should be rounded down.

The operations performed on the min-heap here are push and pop

-   **Push**: When adding a new element, ensure the position of the child, `length of internal heap - 1` is greater than or equal to its parent. If not, continuosly percolate the child up by swapping its value with the parent until the condition has been met. This ensures that the structure and order properties are still valid
-   **Pop**: Removing an element from the top min-heap involves maintaining the structure and order balance of the heap after popping the element. When the length of the heap is 2, the topmost element can simply be popped off and returned. Now in the case where there are children, certain conditions need to be met in order to maintain the properties discussed above. The conditions must be constantly checked while the left child exists, since the heap is a complete binary tree, `while left child exists`
    -   Keep the current topmost element in a temporal buffer, and replace the topmost element is with the last element in the min-heap. Now the new topmost element will be the previously largest element in the left side of the heap. Make sure to remove the element that was previously at the last position since it has now been moved
    -   If right child is present, check for following conditions to know whether is it the legitimate candidate for the swap. First run a check to ensure that the right child is lesser than the left child and it is also lesser than the parent. if satistied, the parent and right child should be swapped then update the index pointer's value to the new position of the swapped parent, `2 * i + 1`
    -   If the left child is lesser than the parent, swap them and update the index pointer to `2 * i`
    -   Terminate the loop, if otherwise. This case is met only when the node is at its final position but not necessarily the last level of the heap
