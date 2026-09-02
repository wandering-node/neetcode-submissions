class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        nodes = set([i for i in range(n)])
        visited = set([])
        for i in range(n):
            if i in visited:
                continue
            queue = collections.deque([i])
            visited.add(i)
            ans += 1
            while queue:
                curr = queue.popleft()
                for nei in adj[curr]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append(nei)
        return ans


