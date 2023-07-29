from common_data_structure import *
from typing import *

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorderIndex = 0
        def construct(preorder, inorder, inStart, inEnd):
            nonlocal preorderIndex
            
            if inStart > inEnd:
                # No child index is outside of the range
                return None
            
            node = TreeNode(preorder[preorderIndex])
            preorderIndex += 1
            if inStart == inEnd:
                # No child, just return the current node
                return node
            
            foundIndex = inorder.index(node.val)
            
            node.left = construct(preorder, inorder, inStart, foundIndex - 1)
            node.right = construct(preorder, inorder, foundIndex + 1, inEnd)
            
            return node
        return construct(preorder, inorder, 0, len(inorder) - 1)

s = Solution()
tree = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
inorder(tree)

tree = s.buildTree([-1], [-1])
inorder(tree)