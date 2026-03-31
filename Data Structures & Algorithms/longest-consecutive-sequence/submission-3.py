class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return len(nums)
        
        # nums.sort()
        # count = 1
        # _max = 0

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         count += 1
        #     elif nums[i] == nums[i-1]:
        #         continue
        #     else:
        #         count = 1
        #     _max = max(_max, count)
            
        # return max(_max, count)

        # above is O(n logn) --> due to sorting

        # below is O(n) but requires extra space

        if len(nums) <= 1:
            return len(nums)
        
        _set = set(nums)
        _max = 0
        

        for n in _set:
             if n - 1 not in _set:
                length = 1
                while (n + length) in _set:
                    length += 1

                _max = max(_max, length)
        
        return _max




            




                
        
        