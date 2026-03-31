class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0

        def pali(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):

            # odd length
            left, right = i, i
            pali(left, right)

            # even length
            left, right = i, i+1
            pali(left, right)
        
        return self.count