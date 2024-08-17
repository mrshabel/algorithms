class ListNode:
    def __init__ (self, val: int=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next

class LinkedList:
    _head = None
    _tail = None

    def appendToHead(self, node_val: int) -> None:
        """
        Append a node to the head of the linked list
        """

        # create node to append
        node = ListNode(val=node_val)

        # keep track of previous head
        current = self._head
        self._head = node
        self._head.next = current




    def appendToTail(self, node_val: int) -> None:
        """
        Append a node to the end of a linked list  
        """

        # create node to append
        node = ListNode(val=node_val)

        # handle case for empty linked list
        if not self._head:
            self._head = node
            self._tail = node

            return

        # constant time operation to update tail without traversing the entire list
        self._tail.next = node
        self._tail = self._tail.next

    
    def traverse(self) -> None:
        """
        Traverse the entire linked list
        """
        # keep initial pointer to head node
        current = self._head

        while current:
            # process node
            print(current.val)
            # update pointer
            current = current.next
    
    def removeByValue(self, val: int) -> None:
        """
        Remove the first occurrence of a node with the specified value in the linked list
        """
        # initialize pointer
        current: ListNode | None = self._head
        dummy: ListNode = ListNode()

        if not current:
            return
        
        # handle special case where value is either at head or tail
        if val == self._head.val:
            self.removeHead()
            return
        
        if val == self._tail.val:
            self.removeTail()
            return
        
        while current.next:
            if val == current.next.val:
                dummy.next = current.next
                current = None
                return
            
            dummy = current
            current = current.next


    def removeHead(self) -> None:
        """
        Remove the head of the linked list
        """
        current = self._head
        if not current:
            return
        
        self._head = current.next
        current = None

    def removeTail(self) -> None:
        """
        Remove the tail of the linked list
        """
        current = self._head

        if not current:
            return
        
        dummy = ListNode()
        
        while current.next:
            dummy = current
            current = current.next
        
        dummy.next = None
        self._tail = dummy
        