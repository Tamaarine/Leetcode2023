from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root : TreeNode):
    if root != None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root : TreeNode):
    if root != None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root : TreeNode):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def initialize_tree_non_full(nums: List[int]):
    queue = deque()
    
    if nums == []:
        return None
    
    root = TreeNode(nums[0])
    queue.append(root)
    
    i = 1
    while len(queue) > 0:
        node = queue.popleft()
        if i < len(nums):
            left = nums[i]
            if left:
                left_node = TreeNode(left)
                node.left = left_node
                queue.append(left_node)
            i += 1
        if i < len(nums):
            right = nums[i]
            if right:
                right_node = TreeNode(right)
                node.right = right_node
                queue.append(right_node)
            i += 1
    return root

def initialize_tree_recursive(nums: List[int], currIndex, n):
    if currIndex >= n:
        return None
    
    # Otherwise currIndex is valid and should be constructed
    root = TreeNode(nums[currIndex])
    root.left = initialize_tree_recursive(nums, 2*currIndex + 1, n)
    root.right = initialize_tree_recursive(nums, 2*currIndex + 2, n)
    
    return root

def initialize_tree(nums : List[int]):
    # We will do it using a queue
    queue = deque()
    
    if nums == []:
        return None
    
    root = TreeNode(nums[0])
    queue.append(root)
    i = 1
    while len(queue) > 0:
        node : TreeNode = queue.popleft()
        
        if i < len(nums):
            left_node = TreeNode(nums[i])
            node.left = left_node
            i += 1
            queue.append(left_node)
        if i < len(nums):
            right_node = TreeNode(nums[i])
            node.right = right_node
            i += 1
            queue.append(right_node)
    return root
