class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort = sorted(heights)
        count = 0
        
        for i, j in zip(heights, sort):
            if i != j:
                count += 1
        
        return count