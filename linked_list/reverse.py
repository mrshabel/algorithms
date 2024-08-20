from linked_list import LinkedList

def reverse(data: LinkedList) -> None:
    """
    Reverse the nodes of a given linked list
    """
    # early return
    if not data:
        return

    # set initial previous pointer to null
    previous = None

    # define tail pointer as current head and set the current pointer
    data._tail = data._head
    current = data._head

    while current:
        # keep track of next pointer as link to it will be broken
        next = current.next

        # update the next pointer of the current node to the previous node
        current.next = previous

        # update the previous node to hold the current node for the next iteration
        previous = current

        # update head pointer to the current node
        data._head = current
        
        # update current pointer
        current = next

if __name__ == "__main__":
    list = LinkedList()
    list.appendToTail(1)
    list.appendToTail(2)
    list.appendToTail(3)
    list.appendToTail(4)
    list.appendToTail(5)
    list.appendToTail(6)

    # reverse the list
    reverse(list)

    # traverse the list
    list.traverse()