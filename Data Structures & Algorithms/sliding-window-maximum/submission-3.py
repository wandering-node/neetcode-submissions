class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxH = []
        res = []
        for i, num in enumerate(nums):
            # remove outdated
            while maxH and maxH[0][1] <= i - k:
                heapq.heappop(maxH)

            # remove older and smaller
            while maxH and -maxH[0][0] < num:
                heapq.heappop(maxH)
            heapq.heappush(maxH, (-num, i))
            if i < k - 1:
                continue
            else:
                res.append(-maxH[0][0])
        return res
