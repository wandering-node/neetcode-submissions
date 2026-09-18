class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        count = 0
        for interval in intervals[1:]:
            if interval[0] < prev_end:
                count += 1
            else:
                prev_end = interval[1]
        return count
