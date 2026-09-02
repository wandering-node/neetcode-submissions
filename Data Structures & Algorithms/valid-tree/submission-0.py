class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        # get all the edges in the graph
        edge_map = collections.defaultdict(list)
        for n1, n2 in edges:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)
        
        visited = set([0])
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in edge_map[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
            
        return len(visited) == n