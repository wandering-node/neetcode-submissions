# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            # first element in preorder list is always the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            # get root index in the original preorder list using the O(1) look-up table
            root_idx = inorder_map[root_val]
            left_size = root_idx - in_start
            
            root.left = helper(pre_start + 1, pre_start + left_size, in_start, in_start + left_size - 1)
            root.right = helper(pre_start + left_size + 1, pre_end, in_start + left_size + 1, in_end)
            return root
        return helper(0, len(preorder) -1, 0, len(inorder) -1 )
