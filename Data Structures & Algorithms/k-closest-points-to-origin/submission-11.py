class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for idx, (x, y) in enumerate(points):
            d = x**2 + y**2
            if len(queue) < k:
                heapq.heappush(queue, (-d, idx))
            elif d < -queue[0][0]:
                heapq.heapreplace(queue, (-d, idx))
        res = [points[idx] for _, idx in queue]
        return res
