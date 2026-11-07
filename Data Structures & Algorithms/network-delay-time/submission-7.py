class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay_map = defaultdict(list)
        for u, v, t in times:
            delay_map[u].append((v, t))

        minH = [(0, k)]
        visited = set()
        max_time = 0
        while minH:
            time, curr = heapq.heappop(minH)
            if curr not in visited:
                max_time = time
                visited.add(curr)
                for nei, lag in delay_map[curr]:
                    if nei not in visited:
                        new_time = time + lag
                        heapq.heappush(minH, (new_time, nei))
        return max_time if len(visited) == n else -1
