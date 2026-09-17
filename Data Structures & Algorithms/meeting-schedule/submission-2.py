"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        prev = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < prev:
                return False

            else:
                prev = end
        return True