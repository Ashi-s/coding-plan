class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l, r = 0, 0
        _max = 0

        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1
            # length of the window 
            length = r - l + 1
            if (length - max(d.values())) <= k:           
                r += 1
                _max = max(_max, (r-l))
            else:
                
                d[s[l]] -= 1
                d[s[r]] -= 1
                l += 1
            
            print(l, r, _max, d)
        
        return _max