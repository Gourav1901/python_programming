def nth_node_from_end(head, n):
    slow = head
    fast = head
    for i in range(n):
        if fast is None:
            return None
        fast = fast.next

    
    while fast is not None:
        slow = slow.next
        fast = fast.next

   
    return slow