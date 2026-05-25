class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_f = 0
        res = 0
        d = {}

        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1


            max_f = max(max_f, d[s[r]])

            if (r-l+1) - max_f <= k:
                res = max(res, r-l+1)
            else:
                while (r-l+1) - max_f > k:
                    d[s[l]] -= 1
                    l += 1
            r += 1
        
        return res