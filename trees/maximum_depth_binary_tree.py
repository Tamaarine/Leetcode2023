from common_data_structure import *
from typing import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        def max_depth(root, height):
            if root == None:
                return height
            
            left_height = height
            right_height = height
            if root.left != None:
                left_height = max_depth(root.left, height + 1)
            if root.right != None:
                right_height = max_depth(root.right, height + 1)
            return max(left_height, right_height)
        return max_depth(root, 1)

s = Solution()
list1 = [3, 9, 20, None, None, 15, 7]
tree = initialize_tree_recursive_non_full(list1, 0, len(list1))
print(s.maxDepth(tree))

list1 = [1, None, 2]
tree = initialize_tree_recursive_non_full(list1, 0, len(list1))
print(s.maxDepth(tree))

list1 = [1]
tree = initialize_tree_recursive_non_full(list1, 0, len(list1))
print(s.maxDepth(tree))