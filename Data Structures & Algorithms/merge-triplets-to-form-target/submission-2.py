class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ind_a = ind_b = ind_c = 0
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                ind_a = 1
            if b == target[1]:
                ind_b = 1
            if c == target[2]:
                ind_c = 1
        return bool(ind_a & ind_b & ind_c)