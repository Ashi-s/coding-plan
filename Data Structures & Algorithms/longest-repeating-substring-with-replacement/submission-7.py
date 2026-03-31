class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        res = 0

        l = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1

            _max = max(d.values())
            if (r - l + 1) - _max <= k:
                res = max(res, (r - l + 1))
            else:
                while (r - l + 1) - _max > k:
                    d[s[l]] -= 1
                    l += 1
        
        return res
        