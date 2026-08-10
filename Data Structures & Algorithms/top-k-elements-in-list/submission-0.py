class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        return [i for i, j in counter.most_common(k)] 