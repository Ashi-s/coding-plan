class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        _set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in _set:
                _set.remove(s[l])
                l += 1
            _set.add(s[r])
            _max = max(_max, r-l+1)
        
        return _max