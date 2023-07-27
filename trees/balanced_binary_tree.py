from common_data_structure import *
from typing import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return True, 0
            
            left_balanced, height_left = dfs(node.left)
            right_balanced, height_right = dfs(node.right)
            
            if not left_balanced or not right_balanced or abs(height_left - height_right) > 1:
                return False, max(height_left, height_right) + 1
            return True, max(height_left, height_right) + 1
        return dfs(root)[0]

s = Solution()
input1 = [1, 2, 2, 3, 3, None, None, 4, 4]
tree = initialize_tree_non_full(input1, 0, len(input1))
print(s.isBalanced(tree))

input1 = [1,2,2,3,None,None,3,4,None,None,4]
tree = initialize_tree_non_full(input1, 0, len(input1))
print(s.isBalanced(tree))