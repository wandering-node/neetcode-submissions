class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        for c, pre in prerequisites:
            edges[c].append(pre)
        visited = {}
        seq = []
        def has_circle(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for nei in edges[node]:
                if has_circle(nei):
                    return True
            visited[node] = False
            seq.append(node)
            return False
        for i in range(numCourses):
            if has_circle(i):
                return []
        return seq
