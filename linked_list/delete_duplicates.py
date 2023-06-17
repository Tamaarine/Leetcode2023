from common_datstructure import *
from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        curr = head
        prev = head
        prev_unique = dummy
        
        while curr:
            if prev.val != curr.val:
                # Meaning no skip. Only one element
                if prev.next == curr:
                    prev_unique = prev
                    prev = curr
                else:
                    # Skip multiple elements
                    prev_unique.next = curr
                    prev = curr
            if curr.next == None and prev != curr:
                prev_unique.next = None
            curr = curr.next
        return dummy.next

s = Solution()
ls1 = initialize_list([1, 1, 2])
print(s.deleteDuplicates(ls1))

ls2 = initialize_list([1, 1, 2, 2])
print(s.deleteDuplicates(ls2))

ls3 = initialize_list([1,2,3,3,4,4,5])
print(s.deleteDuplicates(ls3))
