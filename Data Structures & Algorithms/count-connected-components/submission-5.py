class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_map = collections.defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        
        part = 0
        visited = set()
        def dfs(node):
            for nei in edge_map[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)
            return
        for i in range(n):
            if i not in visited:
                part += 1
                visited.add(i)
                dfs(i)
        return part