class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def helper(idx, curr, res):
            # print(curr)
            if idx > len(s) and len(curr) > 4:
                return
            if len(curr) == 4 and idx == len(s):
                res.append('.'.join(curr.copy()))
                return
            

            for j in range(idx, len(s)):
                # print(len(str(int(s[idx:j+1]))), s[idx:j+1])
                if 0 <= int(s[idx:j+1]) <= 255 and len(str(int(s[idx:j+1]))) == len(s[idx:j+1]):
                    curr.append(s[idx:j+1])
                    helper(j+1, curr, res)
                    curr.pop()
        


        res = []
        for i in range(len(s)):
            if 0 <= int(s[:i+1]) <= 255  and len(str(int(s[:i+1]))) == len(s[:i+1]):
                helper(i+1, [s[:i+1]], res)
        
        return res