# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            max_diameter = max(max_diameter, right + left)
            return max(left, right) + 1
        maxDepth(root)
        return max_diameter