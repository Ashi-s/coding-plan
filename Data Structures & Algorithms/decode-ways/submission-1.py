class Solution:
    def numDecodings(self, s: str) -> int:

        def helper(i):
            if i == len(s):
                self.count += 1
                return
            if i > len(s):
                return
            
            #select 1 char
            if 1 <= int(s[i]) <=26:
                helper(i+1)
            else: # if one digit alone is 0
                return

            # select 2 char (i+2) because last char is not included
            if (i+1) < len(s) and 1 <= int(s[i:i+2]) <= 26:
                helper(i+2)            

        # edge case
        if s and s[0] == '0':
            return 0
        self.count = 0
        helper(0)
        return self.count