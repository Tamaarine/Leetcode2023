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
    
def reverse_link_list(list):
    return _reverse_link_list(list, None)

def _reverse_link_list(curr, prev):
    if curr != None:
        next = curr.next
        curr.next = prev
        return _reverse_link_list(next, curr)
    return prev

def initialize_list(nums):
    dummy = ListNode(0)
    
    curr = dummy
    for num in nums:
        to_add = ListNode(num)
        curr.next = to_add
        curr = to_add
    return dummy.next

def middle_list(list):
    slow = list
    fast = list
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

