class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 > stone2:
                newstone = -stone1 + stone2
                heapq.heappush(heap, newstone)
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
