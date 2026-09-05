class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        edge_map = collections.defaultdict(list)
        for u,v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        
        visited = set([0])
        queue = collections.deque([0])
        while queue:
            curr = queue.popleft()
            for item in edge_map[curr]:
                if item in visited:
                    continue
                else:
                    queue.append(item)
                    visited.add(item)
        return len(visited) == n