class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = collections.defaultdict(list)
        for c, p in prerequisites:
            pre_map[c].append(p)
        
        course_status = {}
        course_seq = []
        def has_circle(course):
            if course in course_status:
                return course_status[course]
            course_status[course] = True
            for pre in pre_map[course]:
                if has_circle(pre):
                    return True
            course_status[course] = False
            course_seq.append(course)
            return False
        
        for c in range(numCourses):
            if has_circle(c):
                return []
        return course_seq