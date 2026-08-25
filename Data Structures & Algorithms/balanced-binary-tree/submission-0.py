# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            height_l = height(node.left)
            if height_l == -1:
                return -1
            height_r = height(node.right)
            if height_r == -1:
                return -1
            if abs(height_l - height_r) > 1:
                return -1
            return 1 + max(height_l, height_r)
        return height(root) != -1        
        