class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_map = collections.defaultdict(list)
        for u,v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        part = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                part += 1
                queue = collections.deque([i])
                while queue:
                    curr = queue.popleft()
                    for nei in edge_map[curr]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
        return part