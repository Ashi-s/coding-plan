class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        _set = set()

        while r < len(s):
            if s[r] not in _set:
                _set.add(s[r])
                res = max(res, r-l+1)
                r += 1
            else:
                while s[r] in _set:
                    _set.remove(s[l])
                    l += 1
        
        return res
