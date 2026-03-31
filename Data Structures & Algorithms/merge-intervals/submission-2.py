class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])

        i = 1
        print(intervals)
        while i < len(intervals):
            print(res)
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                tmp = res.pop()
                res.append([min(tmp[0], intervals[i][0]), max(tmp[1], intervals[i][1])])
            i += 1
        
        return res
            

