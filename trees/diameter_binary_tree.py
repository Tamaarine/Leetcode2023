from common_data_structure import *
from typing import *

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        if root == None:
            return 0
        
        def dfs(root):
            nonlocal res
            
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1
        dfs(root)
        return res

s = Solution()
tree = initialize_tree_non_full([1, 2, 5, 4, None, None, None, 6])
print(s.diameterOfBinaryTree(tree))

tree = initialize_tree_non_full([1, 2, None, 4, None, 6, None])
print(s.diameterOfBinaryTree(tree))

tree = initialize_tree_non_full([])
print(s.diameterOfBinaryTree(tree))

tree = initialize_tree_non_full([1, 2])
print(s.diameterOfBinaryTree(tree))
