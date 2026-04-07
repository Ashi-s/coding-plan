class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = 0
        count = 0

        for i in nums:
            if i != 1:
                count = 0
            else:
                count += 1
                _max = max(_max, count)
        
        return _max
