class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = {}
        # for n in nums:
        #     d[n] = d.get(n, 0) + 1
        
        # return max(d, key=d.get)

        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            
            if res == num:
                count += 1
            else:
                count -= 1
        
        return res
        