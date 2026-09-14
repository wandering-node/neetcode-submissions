class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)

                return res + intervals[i:]
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res