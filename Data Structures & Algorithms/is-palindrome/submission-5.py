class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = [c.lower() for c in s if c.isalnum()]
        # return s == s[::-1]

        # 2 pointer
        l, r = 0, len(s) - 1

        while l < r:
            # if s[l] == " ":
            #     l += 1
            # elif s[r] == " ":
            #     r -= 1
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            
        return True



        