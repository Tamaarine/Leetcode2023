from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        curr = self
        out = ""
        while curr != None:
            out += str(curr.val) + " -> "
            curr = curr.next
        out += "_"
        return out
    
    def __repr__(self):
        return self.__str__()
class Solution:
    # A straightfoward solution from my perspective
    # But the better approach is shown in the next solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # A list that map the index to the next the node has
        map_to_curr = []
        map_to_next = []
        
        curr = head
        while curr != None:
            map_to_curr.append(curr)
            map_to_next.append(curr.next)
            curr = curr.next
    
        if len(map_to_next) == 0 or n > len(map_to_next):
            return None
        if n == len(map_to_next):
            return head.next
        if n == 1:
            if len(map_to_next) == 1:
                return None
            else:
                map_to_curr[-n - 1].next = map_to_next[-n]
                return head
        else:
            map_to_curr[-n - 1].next = map_to_next[-n]
            return head

class Solution2:
    # Apparently slower than my implementation rofl
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy slow and fast pointer
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        for i in range(n):
            fast = fast.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

s = Solution2()

n1 = ListNode(1)
n2 = ListNode(2)

n1.next = n2
# print(s.removeNthFromEnd(n1, 4))
# print(s.removeNthFromEnd(n1, 1))
print(s.removeNthFromEnd(n1, 1))
        