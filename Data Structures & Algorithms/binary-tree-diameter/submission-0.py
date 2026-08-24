# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def getDepth(node: Optional[TreeNode]) -> int:
            nonlocal max_depth
            if not node:
                return 0
            left = getDepth(node.left)
            right = getDepth(node.right)
            max_depth = max(max_depth, left+right)
            return 1 + max(left, right)
        getDepth(root)
        return max_depth