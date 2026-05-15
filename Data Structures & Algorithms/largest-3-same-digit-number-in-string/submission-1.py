class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                if res == "":
                    res = num[i-2:i+1]
                else:
                    res = max(res, num[i-2:i+1])
        
        return res