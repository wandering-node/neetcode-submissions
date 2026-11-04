import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        for idx, num in enumerate(nums):
            while q and q[0][0] <= (idx - k):
                q.popleft()
            while q and q[-1][1] <= num:
                q.pop()
            q.append((idx, num))
            if idx >= k - 1:
                res.append(q[0][1])
        return res
