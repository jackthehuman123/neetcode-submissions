"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sort_int = sorted(intervals, key=lambda x: x.start)

        ends = []
        heapq.heappush(ends, sort_int[0].end)
        count = 1

        for i in sort_int[1:]:
            while ends and ends[0] <= i.start:
                heapq.heappop(ends)
            heapq.heappush(ends, i.end)                
            count = max(count, len(ends))
        return count