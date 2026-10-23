class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            graph[u].append((v, t))

        minH = [(0, k)]
        maxTime = 0
        visited = set()
        while minH:
            time, node = heapq.heappop(minH)
            if node not in visited:
                visited.add(node)
                maxTime = max(maxTime, time)

                for des, lag in graph[node]:
                    if des not in visited:
                        heapq.heappush(minH, (maxTime + lag, des))
        return maxTime if len(visited) == n else -1
