class Solution:
    def longestPalindrome(self, s: str) -> int:
        _set = set()
        res = 0

        for c in s:
            if c in _set:
                _set.remove(c)
                res += 2
            else:
                _set.add(c)
        
        return res + 1 if len(_set) > 0 else res
            