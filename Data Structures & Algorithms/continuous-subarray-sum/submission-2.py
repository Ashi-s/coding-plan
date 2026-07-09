class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # O (n2)
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     for j in range(i+1, len(nums)):
        #         curr += nums[j]
        #         if curr % k == 0:
        #             return True
        
        # return False

        # O(n)
        d = {0:-1} # remainder : index
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            mod = total % k

            if mod not in d:
                d[mod] = i
            else:
                if i - d[mod] >= 2:
                    return True
        return False