class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = [i for i in range(len(edges) + 1)]

        def find(i):
            if roots[i] != i:
                roots[i] = find(roots[i])
            return roots[i]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u, v]
           
            roots[root_u] = root_v