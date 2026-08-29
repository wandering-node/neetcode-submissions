# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = float('-inf')

        def maxGain(node):
            nonlocal path_sum
            if not node:
                return 0
            # if the max path sum in any subtree is negative, we simply don't want it in our path so the gain can only be 0
            left = max(maxGain(node.left), 0)
            right = max(maxGain(node.right), 0)
            path_sum = max(path_sum, left + node.val + right)
            return node.val + max(left, right)

        maxGain(root)
        return path_sum
