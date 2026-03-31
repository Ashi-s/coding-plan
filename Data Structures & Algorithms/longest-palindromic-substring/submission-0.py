class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def pali(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.maxLen:
                    self.maxLen = r - l + 1
                    self.idx = l
                l -= 1
                r += 1
        
        self.idx = 0
        self.maxLen = 0
        for i in range(len(s)):

            # odd length
            left, right = i, i
            pali(left, right)

            # even length
            left, right = i, i+1
            pali(left, right)

        
        return s[self.idx : self.idx + self.maxLen]
