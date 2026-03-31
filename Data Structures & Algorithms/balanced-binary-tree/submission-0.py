# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        self.height(root)
        return self.balance
    
    def height(self, node):
        if not node:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)

        if abs(left - right) > 1:
            self.balance = False

        return 1 + max(left, right)
        