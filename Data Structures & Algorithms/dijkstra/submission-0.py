class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)
        for u, v, d in edges:
            graph[u].append((v, d))
        
        res = {}
        for i in range(n):
            res[i] = float('inf')

        minH = [(0, src)]

        while minH:
            path, u = heapq.heappop(minH)
            while graph[u]:
                v, d = graph[u].pop()
                heapq.heappush(minH, (path + d, v))
            res[u] = min(res[u], path)
        final_res = {}
        for node, dist in res.items():
            final_res[node] = dist if dist != float('inf') else -1
        return final_res


        