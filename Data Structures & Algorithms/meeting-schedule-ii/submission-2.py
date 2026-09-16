"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # sort by start value of the meetings
        intervals.sort(key=lambda x: x.start)
        # track end time of the meetings
        rooms = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if rooms and start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            
        return len(rooms)

