class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # from collections import Counter
        # # simple edge case when nums is empty
        # if len(nums) == 0:
        #     return False
        # ctr = Counter(nums)
        # # get list of the most common 1 element, then compare the occurrence with 1 
        # return ctr.most_common(1)[0][1] > 1

        # solution 2
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False