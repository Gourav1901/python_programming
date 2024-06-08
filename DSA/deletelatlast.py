def remove_last_node(=self,head):
  if head is None:
    return

  current_node = head
  while current_node.next.next:
    