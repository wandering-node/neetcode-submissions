class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        if len(nums) == 0:
            return False
        ctr = Counter(nums)
        return ctr.most_common(1)[0][1] > 1