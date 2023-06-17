from common_datstructure import *
from typing import *

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        curr = dummy.next
        prev = dummy
        while curr != None:
            next = curr.next
            
            # If there is at least two nodes in it left to swap
            # Get temp
            if next != None:
                temp = next.next
                prev.next = next
                next.next  = curr
                curr.next = temp
            
                prev = curr
                curr = temp
            else:
                curr = next
        return dummy.next

s = Solution()
ls1 = initialize_list([1, 2, 3, 4])
print(s.swapPairs(ls1))

ls2 = initialize_list([1, 2])
print(s.swapPairs(ls2))
