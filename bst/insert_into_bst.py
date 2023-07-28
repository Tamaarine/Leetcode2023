from common_data_structure import *
from typing import *

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        def insertBST(parent, curr):
            if curr == None:
                if parent.val > val:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                return
            
            if curr.val > val:
                insertBST(curr, curr.left)
            else:
                insertBST(curr, curr.right)
        insertBST(root, root)            
        return root
    
s = Solution()
# tree = initialize_tree_non_full([4, 2, 7, 1, 3])
# s.insertIntoBST(tree, 5)
# inorder(tree)

tree = initialize_tree_non_full([])
s.insertIntoBST(tree, 5)
inorder(tree)