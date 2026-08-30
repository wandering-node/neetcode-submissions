# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque([root])
        ans = []
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.pop()
                if curr:
                    level.append(curr.val)
                    queue.appendleft(curr.left)
                    queue.appendleft(curr.right)
            if level:
                ans.append(level)
        return ans