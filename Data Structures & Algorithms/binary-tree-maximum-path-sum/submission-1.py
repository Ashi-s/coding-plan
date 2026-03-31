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
            left = max(left, 0)
            right = max(right, 0)


            self.maxPath = max(self.maxPath, left + right + node.val)

            return node.val + max(left, right)
        
        self.maxPath = float('-inf')
        height(root)
        return self.maxPath
        