class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        res = []
        for k, v in d.items():
            if v > len(nums) // 3:
                res.append(k)
        
        return res