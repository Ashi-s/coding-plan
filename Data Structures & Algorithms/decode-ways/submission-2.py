class Solution:
    def numDecodings(self, s: str) -> int:

        # solution 1 - Recursion
        # def helper(i):
        #     if i == len(s):
        #         self.count += 1
        #         return
        #     if i > len(s):
        #         return
            
        #     #select 1 char
        #     if 1 <= int(s[i]) <=26:
        #         helper(i+1)
        #     else: # edge case - if one digit alone is 0 and this also skips the next call(down below) which would be "01"or and any "0x"
        #         return

        #     # select 2 char (i+2) because last char is not included
        #     if (i+1) < len(s) and 1 <= int(s[i:i+2]) <= 26:
        #         helper(i+2)            

        # # edge case
        # if s and s[0] == '0':
        #     return 0

        # self.count = 0
        # helper(0)
        # return self.count

        # Solution 2 - DP
        memo = {len(s): 1}
        def helper(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            if i > len(s):
                return 0
            
            if 1 <= int(s[i]) <=26:
                res = helper(i+1)
            
            if (i+1) < len(s) and 1 <= int(s[i:i+2]) <= 26:
                res += helper(i+2)  

            memo[i] = res
            return res

        return helper(0) 
            

