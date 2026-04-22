# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            left = max(0, left)
            right = max(0, right)

            self.res = max(self.res, left + right + node.val)

            return node.val + max(left, right)
        
        self.res = float('-inf')
        height(root)
        return self.res