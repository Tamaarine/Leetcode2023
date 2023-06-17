from common_datstructure import *
from typing import *

# Very easy solution, easy to implement compared to the reversing a linked list
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        
        while head != None:
            arr.append(head.val)
            head = head.next
        
        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - 1 - i]:
                return False
        return True

class Solution2:
    # Don't bother trying this. Is not worth it, go with the easy way
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
        if count == 1:
            return True
        
        halved = count // 2
        node_count = 0
        curr = head
        next_half = None
        while node_count != halved:
            node_count += 1
            
            if node_count == halved:
                next_half = curr.next
                curr.next = None
            
            curr = curr.next
        if count % 2 == 1:
            next_half = next_half.next
        
        next_half = reverse_link_list(next_half)
        
        # Check if they are equal
        curr = head
        while curr != None:
            if curr.val != next_half.val:
                return False
            curr = curr.next
            next_half = next_half.next
        return True

s = Solution2()
n1 = initialize_list([1, 2, 3, 4])
n2 = initialize_list([1, 1, 2, 2])
n3 = initialize_list([1])
n3 = initialize_list([1, 1, 1])
n4 = initialize_list([1, 2, 1])
n5 = initialize_list([1, 2, 1])
n6 = initialize_list([1, 2, 1, 2])
print(s.isPalindrome(n1))
print(s.isPalindrome(n2))
print(s.isPalindrome(n3))
print(s.isPalindrome(n4))
print(s.isPalindrome(n5))
print(n6)
print(s.isPalindrome(n6))
