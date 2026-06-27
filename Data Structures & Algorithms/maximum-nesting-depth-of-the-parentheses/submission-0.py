class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        res = 0

        for i in s:
            if i == '(':
                curr += 1
            elif i == ')':
                curr -= 1
            res = max(res, curr)
        return res