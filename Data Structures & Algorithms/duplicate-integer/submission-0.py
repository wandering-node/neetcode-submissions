class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        ctr = Counter(nums)
        return ctr.most_common(1)[0][1] > 1