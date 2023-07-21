from common_data_structure import *
from typing import *

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        
        if root == None:
            return True
        
        # Add in the left and right element of the root
        queue.append(root.left)
        queue.append(root.right)
        
        while len(queue) > 0:
            print(queue)
            # While the queue is not empty, pop the left and right node
            left = queue.popleft()
            right = queue.popleft()
            
            if left is None and right is None:
                # If both is none, there is nothing to do. Continue. No child to add to queue either
                continue
            
            if (left == None or right == None) or (left.val != right.val):
                return False
            
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True
s = Solution()
in1 = [1,2,2,3,4,4,3]
tree = initialize_tree_non_full(in1)
print(s.isSymmetric(tree))

in1 = [1,2,2,None,3,None,3]
tree = initialize_tree_non_full(in1)
print(s.isSymmetric(tree))