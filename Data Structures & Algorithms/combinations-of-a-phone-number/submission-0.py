class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def helper(idx):

            if len(curr) == len(digits):
                res.append(curr.copy())
                return
            
            for c in map[digits[idx]]:
                curr.append(c)
                helper(idx+1)
                curr.pop()
        
        curr = []
        res = []
        helper(0)
        return [''.join(r) for r in res]