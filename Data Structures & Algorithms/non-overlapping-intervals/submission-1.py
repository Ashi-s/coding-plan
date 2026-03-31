class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        if len(intervals) == 1:
            return count
        
        intervals.sort()
        i = 1
        prev = intervals[0]
        while i < len(intervals):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
            else:
                count += 1
                # select the one with min value at index 1 
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
            
            i += 1
        return count