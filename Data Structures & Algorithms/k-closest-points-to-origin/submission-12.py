class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for idx, (x, y) in enumerate(points):
            distance = x**2 + y**2
            if len(heap) < k:
                heapq.heappush(heap, (-distance, idx))
            elif distance < -heap[0][0]:
                heapq.heapreplace(heap, (-distance, idx))
        return [points[heap[i][1]] for i in range(len(heap))]
