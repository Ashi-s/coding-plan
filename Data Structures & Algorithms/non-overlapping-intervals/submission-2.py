class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        if len(intervals) == 1:
            return count
        
        intervals.sort()
        prev = intervals[0]

        i = 1
        while i < len(intervals):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
            else:
                count += 1
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
            i += 1
        
        return count