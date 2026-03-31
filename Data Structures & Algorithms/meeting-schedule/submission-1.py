"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1:
            return True
        intervals.sort(key = lambda x: x.start)
        i = 1
        while i < len(intervals):
            if intervals[i].start >= intervals[i-1].end:
                i += 1
            else:
                return False
            
        
        return True
