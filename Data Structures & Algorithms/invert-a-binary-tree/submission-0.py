# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.helper(root)
        return root
        
    
    def helper(self, root):
        if not root.left and not root.right:
            return
        elif root.left and root.right:
            root.left, root.right = root.right, root.left
            self.helper(root.left)
            self.helper(root.right)
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
            self.helper(root.right)
        elif root.right and not root.left:
            root.left = root.right
            root.right = None
            self.helper(root.left)
        