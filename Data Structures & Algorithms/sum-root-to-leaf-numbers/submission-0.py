# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, curr, res):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(int(curr))
                return
            
            if node.left:
                helper(node.left, curr+str(node.left.val), res)
            
            if node.right:
                helper(node.right, curr+str(node.right.val), res)
        
        res = []
        helper(root, str(root.val), res)
        return sum(res)