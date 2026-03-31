class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l, r = 0, 0
        _max = 0

        # while r < len(s):
        #     d[s[r]] = d.get(s[r], 0) + 1
        #     # length of the window 
        #     length = r - l + 1
        #     if (length - max(d.values())) <= k:           
        #         r += 1
        #         _max = max(_max, (r-l))
        #     else:
                
        #         d[s[l]] -= 1
        #         d[s[r]] -= 1 #imp - when left is increased, next loop adds back same "r" which was already added
        #         l += 1

        #Different way
        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1

            if ((r-l+1) - max(d.values())) <= k:
                _max = max(_max, r-l+1)
            else:
                while (r-l+1) - max(d.values()) > k:
                    d[s[l]] -= 1
                    l += 1
            r += 1
         
        return _max