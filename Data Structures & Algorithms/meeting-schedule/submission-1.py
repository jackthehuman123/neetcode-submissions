"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = True
        sort_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(sort_intervals) - 1):
            if sort_intervals[i].end > sort_intervals[i+1].start:
                res = False
        return res