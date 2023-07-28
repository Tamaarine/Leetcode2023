from common_data_structure import *
from typing import *

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        def inorder(root):
            nonlocal k, res
            if root != None:
                inorder(root.left)
                k -= 1
                if k == 0:
                    res = root.val
                inorder(root.right)
        inorder(root)
        return res

s = Solution()
tree = initialize_tree_non_full([3, 1, 4, None, 2])
print(s.kthSmallest(tree, 1))

tree = initialize_tree_non_full([5, 3, 6, 2, 4, None, None, 1])
print(s.kthSmallest(tree, 3))
