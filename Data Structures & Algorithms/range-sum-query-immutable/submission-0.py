class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumByIndex = []

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.sumByIndex.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.sumByIndex[right]
        leftSum = self.sumByIndex[left - 1] if left > 0 else 0

        return rightSum - leftSum
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)