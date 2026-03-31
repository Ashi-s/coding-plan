class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):

            while l >=0 and r < n and s[l] == s[r]:
                if (r-l+1) > self.maxLen:
                    self.maxLen = r-l+1
                    self.idx = l
                l -= 1
                r += 1


        self.maxLen = 0
        self.idx = 0
        n = len(s)
        for i in range(n):

            # odd length
            l, r = i, i
            isPalindrome(l, r)

            # even length
            l, r = i, i+1
            isPalindrome(l, r)
        
        return s[self.idx:self.idx + self.maxLen]