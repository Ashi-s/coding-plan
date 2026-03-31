# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, curr, maximum):
            if not node:
                return
            
            if node.val >= maximum:
                curr.append(node.val)
            
            helper(node.left, curr, max(maximum, node.val))
            helper(node.right, curr, max(maximum, node.val))
        

        if not root:
            return []
        output = []
        helper(root, output, root.val)
        # print(output)
        return len(output)