class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        res = []
        res.append(intervals[0])

        i = 1
        while i < len(intervals):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                tmp = res.pop()
                res.append([min(tmp[0], intervals[i][0]), max(tmp[1], intervals[i][1])])
            i += 1
        
        return res
            

