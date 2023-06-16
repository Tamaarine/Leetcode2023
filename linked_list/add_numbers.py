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
    # Simple enough. Just need to care about the carry and bring it to the next adding
    # Also be careful with remaining carrys 99 + 1
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        cur = dummy
        carry = 0
        while l1 != None and l2 != None:
            total = l1.val + l2.val + carry
            carry = total // 10
            total %= 10
            
            to_add = ListNode(total)
            cur.next = to_add
            cur = to_add
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            total = l1.val + carry
            carry = total // 10
            total %= 10
            
            to_add = ListNode(total)
            cur.next = to_add
            cur = to_add
            l1 = l1.next
        
        while l2 != None:
            total = l2.val + carry
            carry = total // 10
            total %= 10
            
            to_add = ListNode(total)
            cur.next = to_add
            cur = to_add
            l2 = l2.next
        if carry == 1:
            to_add = ListNode(1)
            cur.next = to_add
            
        return dummy.next

n1 = ListNode(9)
n2 = ListNode(9)

n1.next = n2

n4 = ListNode(1)

s = Solution()
print(s.addTwoNumbers(n1, n4))