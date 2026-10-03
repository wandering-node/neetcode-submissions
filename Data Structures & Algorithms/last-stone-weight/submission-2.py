class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 != stone2:
                newstone = -stone1 + stone2
                heapq.heappush(heap, newstone)
        return -heapq.heappop(heap) if heap else 0
        