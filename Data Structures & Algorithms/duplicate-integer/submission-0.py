class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for n in nums:
            if n not in _set:
                _set.add(n)
            else:
                return True
        return False
        