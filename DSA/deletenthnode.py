class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def nth_node_from_end(head, n):
    slow = head
    fast = head

    # Move fast pointer n steps ahead
    for i in range(n):
        if fast is None:
            # n is greater than the number of nodes
            return None
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # At this point, slow is at the nth node from the end
    return slow

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
n = 2
result_node = nth_node_from_end(head, n)

if result_node:
    print(f"The {n}th node from the end has the value: {result_node.value}")
else:
    print(f"There is no {n}th node from the end in the list.")
