class Heap:
    """
    An implementation of a min-heap that uses an array under the hood
    """
    
    def __init__(self) -> None:
        # place a dummy value, 0 in the first index to maintain the mathematical balance
        self._heap = [0]

    def push(self, val):
        """
        Add a new value to the heap
        """
        # the time complexity of this operation is the height of the heap, log(n), since it is a complete binary tree
        self._heap.append(val)
        index = len(self._heap) - 1

        # percolate up. this is done to maintain the order property by shifting the values
        # the parent is at index `i / 2`
        # child = self._heap[index]
        # parent = self._heap[index // 2]

        # swap the child and parent while the order has not been maintained. thus, child lesser than parent
        while self._heap[index] < self._heap[index // 2]:
            temp = self._heap[index // 2]
            self._heap[index // 2] = self._heap[index]
            self._heap[index] = temp

            # move the index marker to the new parent position
            index = index // 2
    
    def pop(self):
        """
        Remove the top-most element from the heap
        """
        # time complexity for this is the height of the tree
        # check for empty heap
        if len(self._heap) == 1:
            return None
        
        # remove element directly when there is only one node
        if len(self._heap) == 2:
            return self._heap.pop()
        
        # since the element to be removed here is not the root, the root must be replaced with the last element in the heap then percolated down to ensure that the structure and order properties are maintained
        root = self._heap[1]

        # move last value to top of heap
        self._heap[1] = self._heap.pop()
        # keep a pointer for the root node
        index = 1

        # percolate down. 2 * index represents the left child while 2 * index + 1 represents the right child
        while (2 * index) < len(self._heap):
            # case 1: where both children are present.
            # if right child is present and right child is smaller than left child and right child is smaller than parent
            if ((2 * index + 1) < len(self._heap)) and (self._heap[2 * index + 1] < self._heap[2 * index]) and (self._heap[2 * index + 1] < self._heap[index]):
                # swap right child
                temp = self._heap[index]
                self._heap[index] = self._heap[2 * index + 1]
                self._heap[2 * index + 1] = temp

                # update pointer to the right child
                index = 2 * index + 1

            # case 2: where only one child, left child is present and left child is lesser than parent
            elif self._heap[2 * index] < self._heap[index]:
                # swap left child
                temp = self._heap[index]
                self._heap[index] = self._heap[2 * index]
                self._heap[2 * index] = temp

                # update pointer to the left child
                index = 2 * index

            # case 3: where no child is present. this is when the element is in its final position but not at the bottom
            else:
                break

            return root