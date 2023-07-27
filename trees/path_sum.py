from common_data_structure import *
from typing import *

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
    
        
        def dfs(root, target):
            if root == None:
                if target != 0:
                    return False
                else:
                    return True
            if root.left == None and root.right == None:
                return targetSum == root.val
            
            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)
        
        return dfs(root, targetSum)
    
s = Solution()
tree = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree = initialize_tree_non_full(tree)
print(s.hasPathSum(tree, 22))

tree = []
tree = initialize_tree_non_full(tree)
print(s.hasPathSum(tree, 5))
