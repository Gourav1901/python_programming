def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head

        node_set = set()

        while temp is not None:
            if temp in node_set:
                return True
            
            node_set.add(temp)
            temp = temp.next

        return False
        #optimize approach
      # slow = head
      # fast = head

      # while fast != None and fast.next != None:
      #   slow = slow.next
      #   fast = fast.next.next

      #   if fast == slow:
      #       return True

      # return False
