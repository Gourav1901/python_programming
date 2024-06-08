class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def length_of_linked_list(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


    

# Example usage
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    # Finding the length of the linked list
    print("Length of the linked list:", length_of_linked_list(head))
