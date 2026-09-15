class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curr = intervals[0]
        for interval in intervals:
            if curr[1] < interval[0]:
                res.append(curr)
                curr = interval
            # elif curr[0] > interval[1]:
            #     res.append(interval)
            else:
                # curr[0] = min(interval[0], curr[0])
                curr[1] = max(interval[1], curr[1])

        res.append(curr)
        return res