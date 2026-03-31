# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, count, maxVal):
            if not node:
                return

            if node.left:
                if node.left.val >= maxVal :
                    self.count += 1
                    helper(node.left, self.count, max(maxVal, node.left.val))
                else:
                    helper(node.left, self.count, max(maxVal, node.left.val))
            if node.right:
                if node.right.val >= maxVal:
                    self.count += 1
                    helper(node.right, self.count, max(maxVal, node.right.val))
                else:
                    helper(node.right, self.count, maxVal)
        
        self.count = 1
        helper(root, self.count, root.val)
        return self.count
