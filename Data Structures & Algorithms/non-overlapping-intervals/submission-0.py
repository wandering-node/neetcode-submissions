class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        # curr = intervals[0]
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            # no overlap
            if prevEnd <= interval[0]:
                prevEnd = interval[1]
            # with overlap
            else:
                res += 1
                prevEnd = min(interval[1], prevEnd)
        return res

