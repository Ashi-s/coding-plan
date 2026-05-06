class Solution:
    def check(self, nums: List[int]) -> bool:
        # there can be atmost one break point
        # if we find more than 1 then return False

        count = 0
        N = len(nums)
        for i in range(N):
            #why (i+1)%N ? to comparelast index with first index
            if nums[i] > nums[(i+1) % N]:
                count += 1
            
                if count > 1:
                    return False
        
        return True
