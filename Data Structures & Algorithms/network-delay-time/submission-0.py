class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, t in times:
            graph[u].append((v, t))

        minH = [(0, k)]
        visited = set()
        max_time = 0

        while minH:
            time, node = heapq.heappop(minH)

            if node in visited:
                continue
            
            visited.add(node)
            max_time = max(max_time, time)
            for nei, lag in graph[node]:
                if nei not in visited:
                    new_time = time + lag
                    heapq.heappush(minH, (new_time, nei))
        if len(visited) == n:
            return max_time
        return -1