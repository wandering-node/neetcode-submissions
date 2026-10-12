class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minH = []
        intervals.sort()
        ans = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minH, ((intervals[i][1]-intervals[i][0] + 1), intervals[i][1]))
                i += 1
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            ans[q] = minH[0][0] if minH else -1
        return [ans[q] for q in queries]
        
