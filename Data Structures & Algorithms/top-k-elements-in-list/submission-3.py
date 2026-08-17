class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        # the i-th list in freq_map means the numbers appeared i times
        freq_map = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            # get the count of each numbers
            count[num] += 1
        for n, c in count.items():
            freq_map[c].append(n)
        ans = []
        for freq in range(len(freq_map)-1, -1, -1):
            if k > 0:
                ans.extend(freq_map[freq])
                k -= len(freq_map[freq])
        return ans