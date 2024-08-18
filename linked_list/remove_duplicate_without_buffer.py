from . import LinkedList

def remove_duplicate_without_buffer(data: LinkedList) -> None:
    """
    Remove duplicate values from a linked list without using buffer such as a hash set, or hash map

    `Detail`: the runner technique is used by ensuring that two pointers are used to effectively traverse the linked list
    """
    current = data._head

    while current:
        # set up runner to traverse the entire linked list
        runner = current
        while runner.next:
            # skip node if it is a duplicate, thus value at current and runner pointers are the same
            if current.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        # process next node
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

remove_duplicate_without_buffer(list)

list.traverse()