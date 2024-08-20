from . import LinkedList, ListNode, find_middle_node

def delete_middle_node(node: ListNode) -> None:
    """
    Delete the middle node from a linked list where only the node to be deleted is provided with no head to the linked list
    """
    # handle edge cases where node may be tail or may not exist
    if node == None or node.next == None:
        return None
    
    # considering that we have no access to the previous node, we copy the data from the next node to the current node and modify the pointers
    next = node.next
    node.val = next.val
    node.next = next.next

    return node


if __name__ == "main":
    list = LinkedList()
    list.appendToTail(1)
    list.appendToTail(2)
    list.appendToTail(3)
    list.appendToTail(4)
    list.appendToTail(5)
    list.appendToTail(6)

    node = find_middle_node(linked_list=list)

    delete_middle_node(node=node)

    list.traverse()