from . import LinkedList, ListNode

def remove_duplicate(data: LinkedList) -> None:
    """
    Remove all duplicates from an unsorted linked list

    `Detail`: A pointer is used to track the previous node during the iteration of the linked list.
            If a node already exists in the hash set, it is skipped by making sure that the node's previous pointer is set to its next pointer
    """
    visited = set()

    previous: ListNode | None = None
    current = data._head

    while current:
        if current.val in visited:
            previous.next = current.next
            current = current.next
            continue

        visited.add(current.val)
        previous = current
        current = current.next
        

list = LinkedList()
list.appendToTail(1)
list.appendToTail(1)
list.appendToTail(1)
list.appendToTail(2)
list.appendToTail(3)
list.appendToTail(3)
list.appendToTail(4)
list.appendToTail(5)
list.appendToTail(6)
list.appendToTail(6)
list.appendToTail(6)
list.appendToTail(6)

remove_duplicate(list)

list.traverse()