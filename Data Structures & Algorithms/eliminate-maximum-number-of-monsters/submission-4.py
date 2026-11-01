class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # number of monsters
        n = len(dist)
        kill = [0] * n

        for d, s in zip(dist, speed):
            deadline = (d - 1) // s
            if deadline < n:
                kill[deadline] += 1

        need_kill = 0
        for idx, cnt in enumerate(kill):
            need_kill += cnt
            if need_kill > idx + 1:
                return idx + 1

        return n
