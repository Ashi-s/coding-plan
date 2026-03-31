# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # DFS
        def helper(node, left, right):
            if not node:
                return True
            
            if not left < node.val < right:
                return False
            
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        # return helper(root, float('-inf'), float('inf')) 

        # BFS
        def helperBFS(root, left, right):
            if not root:
                return True
            
            q = deque([(root, float('-inf'), float('inf'))])

            while q:
                node, left, right = q.popleft()

                if not left < node.val < right:
                    return False
                
                if node.left:
                    q.append((node.left, left, node.val))
                
                if node.right:
                    q.append((node.right, node.val, right))
            
            return True
        
        return helperBFS(root, float('-inf'), float('inf')) 

        