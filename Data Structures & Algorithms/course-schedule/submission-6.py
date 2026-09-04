class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        pre_map = collections.defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        state = [0] * numCourses
        def has_circle(idx):
            if state[idx] == 1:
                return True
            if state[idx] == 2:
                return False
            state[idx] = 1
            for pre in pre_map[idx]:
                if has_circle(pre):
                    return True
            state[idx] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if has_circle(i):
                    return False
        return True
