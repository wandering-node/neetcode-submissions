class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = collections.defaultdict(list)
        for c, p in prerequisites:
            pre_map[c].append(p)
        
        res = []
        taking = {}
        def has_circle(course):
            if course in taking:
                return taking[course]
            taking[course] = True
            for pre in pre_map[course]:
                if has_circle(pre):
                    return True
            taking[course] = False
            res.append(course)
            return False
        for i in range(numCourses):
            if has_circle(i):
                return []
        return res





