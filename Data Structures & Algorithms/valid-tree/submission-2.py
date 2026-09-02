class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        # get all the edges in the graph
        edge_map = collections.defaultdict(list)
        for n1, n2 in edges:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)

        visited = set([])
        def has_circle(node, parent):
            visited.add(node)
            for n in edge_map[node]:
                if n == parent:
                    continue
                if n in visited:
                    return True
                if has_circle(n, node):
                    return True
            return False

                
                
                

        if has_circle(0, -1):
            return False

        return len(visited) == n
