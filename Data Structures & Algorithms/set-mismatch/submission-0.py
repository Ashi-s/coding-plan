class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        res = [0,0]

        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        for i in range(1, len(nums)+1):
            if d.get(i, 0) == 2:
                res[0] = i
            elif d.get(i, 0) == 0:
                res[1] = i
        
        return res