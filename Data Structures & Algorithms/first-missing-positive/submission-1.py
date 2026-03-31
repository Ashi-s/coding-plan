class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        _set = set(nums)
        res = 1

        for i in range(1, n+1):
            if i not in _set:
                return i
            res = i
        return res + 1
        