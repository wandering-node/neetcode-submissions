class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_map = collections.defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        
        part = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            else:
                visited.add(node)
                for nei in edge_map[node]:
                    dfs(nei)
            return
        for i in range(n):
            if i not in visited:
                part += 1
                dfs(i)
        return part