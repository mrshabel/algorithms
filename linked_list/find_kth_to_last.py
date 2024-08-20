from linked_list import LinkedList, ListNode

def find_kth_to_last(data: LinkedList, k: int) -> ListNode:
    """
    Finds the kth node from the tail node of the linked list

    `Detail`: 2 pointers are defined, p1 and p2, where they are separated by 'k' distance. the pointers are moved progressively until p2 gets to the end
              Considering that p2 is now at the end of the linked list, p1 will be 'k' distance away from the end of the linked list
    """

    p1 = p2 = data._head

    # initially place p2 at a distance k, away from p1
    for _ in range(k):
        if not p2:
            return
        p2 = p2.next
    
    # iterate through the linked list until p2 reaches the end while incrementing both pointers
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    
    # now p1 is at it's final destination, k nodes from the tail
    # process p1
    return p1


if __name__ == "__main__":
    list = LinkedList()
    list.appendToTail(1)
    list.appendToTail(2)
    list.appendToTail(3)
    list.appendToTail(4)
    list.appendToTail(5)
    list.appendToTail(6)

    node = find_kth_to_last(list, 1)

    print(node.val)