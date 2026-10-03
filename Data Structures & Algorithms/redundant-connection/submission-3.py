class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        sizes = [1 for _ in range(len(edges) + 1)]
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u, v]

            if sizes[root_u] > sizes[root_v]:
                parents[root_v] = root_u
                sizes[root_u] += sizes[root_v]
            else:
                parents[root_u] = root_v
                sizes[root_v] += sizes[root_u]