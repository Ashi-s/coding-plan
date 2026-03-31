class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        _set = set(nums)
        res = 1

        for n in nums:
            if n-1 not in _set:
                length = 1
                while (n + length) in _set:
                    length += 1
                
                res = max(res, length)
        
        return res