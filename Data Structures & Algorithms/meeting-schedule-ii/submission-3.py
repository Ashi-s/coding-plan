"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        res = 0
        count = 0

        # METHOD 1  
        # for i in intervals:
        #     times.append((i.start, 1))
        #     times.append((i.end, -1))
        
        # times.sort(key=lambda x: (x[0], x[1]))

        # for t in times:
        #     count += t[1]
        #     res = max(res, count)
        
        # return res

        # METHOD 2
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]

        starts.sort()
        ends.sort()

        s, e = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res



