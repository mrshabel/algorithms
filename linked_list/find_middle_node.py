from linked_list import LinkedList, ListNode

def find_middle_node(linked_list: LinkedList) -> ListNode:
    """
    Find the middle node of a given linked list
    """
    # define two pointers, runner and current where runner moves twice the speed of current
    current = linked_list._head
    runner = linked_list._head

    while runner.next and runner.next.next:
        current = current.next
        runner = runner.next.next
    
    # since runner is now at the end, current will be at the exact middle of the linked list
    return current


if __name__ == "__main__":

    list = LinkedList()
    list.appendToTail(1)
    list.appendToTail(2)
    list.appendToTail(3)
    list.appendToTail(4)
    list.appendToTail(5)
    list.appendToTail(6)

    node = find_middle_node(linked_list=list)

    print(node.val)