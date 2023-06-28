from typing import *
from common_datstructure import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 : List[int] = []
        s2 : List[int] = []
        res : List[int] = []
        carry = 0
        
        curr = l1
        while curr != None:
            s1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr != None:
            s2.append(curr.val)
            curr = curr.next
        
        while s1 and s2:
            n1 = s1.pop()
            n2 = s2.pop()
            result = n1 + n2 + carry
            carry = result // 10
            result %= 10
            res.append(result)
        while s1:
            n = s1.pop() + carry
            carry = n // 10
            n %= 10
            res.append(n)
        while s2:
            n = s2.pop() + carry
            carry = n // 10
            n %= 10
            res.append(n)
        
        if carry != 0:
            res.append(1)
        
        # Reverse the list
        res = res[::-1]
        
        return initialize_list(res)

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 : List[int] = []
        s2 : List[int] = []
        res = None
        carry = 0
        
        curr = l1
        while curr != None:
            s1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr != None:
            s2.append(curr.val)
            curr = curr.next
        
        while s1 and s2:
            n1 = s1.pop()
            n2 = s2.pop()
            result = n1 + n2 + carry
            carry = result // 10
            result %= 10
            
            node = ListNode(result, res)
            res = node
        while s1:
            n = s1.pop() + carry
            carry = n // 10
            n %= 10
            node = ListNode(n, res)
            res = node
        while s2:
            n = s2.pop() + carry
            carry = n // 10
            n %= 10
            node = ListNode(n, res)
            res = node
        
        if carry != 0:
            node = ListNode(1, res)
            res = node
        
        return res
            
s = Solution2()
l1 = initialize_list([7, 2, 4, 3])
l2 = initialize_list([5, 6, 4])
print(s.addTwoNumbers(l1, l2))

l1 = initialize_list([7, 2])
l2 = initialize_list([5, 6, 4])
print(s.addTwoNumbers(l1, l2))

l1 = initialize_list([])
l2 = initialize_list([])
print(s.addTwoNumbers(l1, l2))