class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # time - O(n)  & space O(n)
        # d = {}
        # for n in nums:
        #     d[n] = 1 + d.get(n, 0)
        
        # res = []
        # for k, v in d.items():
        #     if v > len(nums) // 3:
        #         res.append(k)
        
        # return res
        num1, num2 = -1, -1
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        res = []
        if cnt1 > len(nums) // 3:
            res.append(num1)
        if cnt2 > len(nums) // 3:
            res.append(num2)
        
        return res

