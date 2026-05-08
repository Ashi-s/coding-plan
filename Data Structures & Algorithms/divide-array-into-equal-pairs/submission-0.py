class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        for key, val in d.items():
            if val % 2 != 0:
                return False
        return True