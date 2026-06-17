# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node, curr):
            if not node:
                return
            
            if low <= node.val <= high:
                curr[0] = curr[0] + node.val
            
            helper(node.left, curr)
            helper(node.right, curr)
        
        curr = [0]
        helper(root, curr)
        return curr[0]
