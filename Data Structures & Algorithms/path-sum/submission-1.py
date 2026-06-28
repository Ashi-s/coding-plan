# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, total, res):
            if not node:
                return 
            
            if not node.left and not node.right:
                if (total[0] + node.val) == targetSum:
                    res[0] = True
                return
            
            if node.left:
                total[0] += node.val
                helper(node.left, total, res)
                total[0] -= node.val
            
            if node.right:
                total[0] += node.val
                helper(node.right, total, res)
                total[0] -= node.val
        
        res = [False]
        total = [0]
        helper(root, total, res)
        return res[0]
