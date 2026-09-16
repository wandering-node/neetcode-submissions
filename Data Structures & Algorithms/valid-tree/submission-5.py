class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False


        edge_map = collections.defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        queue = collections.deque([0])
        visited = set([0])
        while queue:
            curr = queue.pop()
            for nei in edge_map[curr]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return len(visited) == n
