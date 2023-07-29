from common_data_structure import *
from typing import *

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root == None:
                return True
            
            left_valid = dfs(root.left)
            right_valid = dfs(root.right)
            
            if left_valid and right_valid:
                if root.left and root.left.val >= root.val:
                    return False
                if root.right and root.right.val <= root.val:
                    return False
                return True
            else:
                return False
        
        return dfs(root)

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        res = []
        def inorder(root):
            nonlocal res
            if root != None:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        print(res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

s = Solution2()
tree = initialize_tree_non_full([2, 1, 3])
print(s.isValidBST(tree))

tree = initialize_tree_non_full([5, 1, 4, None, None, 3, 6])
print(s.isValidBST(tree))

tree = initialize_tree_non_full([1, 0, 3])
print(s.isValidBST(tree))