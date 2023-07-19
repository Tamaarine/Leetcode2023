from common_data_structure import *
from typing import *

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        if root == None:
            return []
        
        def tree_paths(node : Optional[TreeNode], path_str):
            if node.left or node.right:
                if node.left:
                    tree_paths(node.left, f"{path_str}{node.val}->")
                if node.right:
                    tree_paths(node.right, f"{path_str}{node.val}->")
            else:
                # Node has no child, it is the end, no recursive call
                paths.append(path_str + str(node.val))
        
        tree_paths(root, "")
        return paths

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)

a.left = b
a.right = c
b.right = d

print(s.binaryTreePaths(a))