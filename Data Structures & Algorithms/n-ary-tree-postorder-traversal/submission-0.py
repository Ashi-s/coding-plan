"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def helper(node):
            if not root:
                return
            
            for ch in node.children:
                helper(ch)
            res.append(node.val)
            

        res = []
        helper(root)
        return res
