class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # early stop if no prerequisites required
        if not prerequisites:
            return True
        # get hash table for easy lookup
        pre_dict = collections.defaultdict(list)
        for course, pre in prerequisites:
            pre_dict[course].append(pre)
        
        state = [0] * numCourses
        def is_circle(course):
            if state[course] == 1:  # 1 is visiting now
                return True # true means a circle is detected
            if state[course] == 2:  # 2 has explored before
                return False # means no circle in the last exploration

            state[course] = 1
            for pre in pre_dict[course]:  #defaultdict can do the loop directly
                if is_circle(pre):
                    return True
            state[course] = 2
            return False
    
        for i in range(numCourses):
            if state[i] == 0:
                if is_circle(i):
                    return False
        return True