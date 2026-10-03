class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            curr_k = self.heap[0]
            if val > curr_k:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
