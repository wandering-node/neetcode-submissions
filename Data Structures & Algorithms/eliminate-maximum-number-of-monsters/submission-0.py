class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = [dist[i] / speed[i] for i in range(len(speed))]
        heapq.heapify(monsters)

        time = kill = 0
        while monsters:
            monster = heapq.heappop(monsters)
            if monster > time:
                time += 1
                kill += 1
            else:
                return kill
        return kill