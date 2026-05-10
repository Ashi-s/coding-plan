class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        count = 0
        for key, val in d.items():
            temp = (val * (val - 1)) // 2
            count += temp
        
        return count
        