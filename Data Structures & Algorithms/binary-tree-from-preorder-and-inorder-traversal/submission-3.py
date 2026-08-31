# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # get the inorder index map for o(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            # [pre_start, pre_end] is the index (inclusive) partition for the sub-tree in the preorder list, same for the [in_start, in_end]
            if pre_start > pre_end or in_start > in_end:
                return
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]
            left_len = root_idx - in_start
            root.left = helper(
                pre_start
                + 1,  # pre_start index is always the root, so the left tree start from pre_start + 1
                pre_start
                + 1
                + left_len
                - 1,  # since end index is inclusive, the index should be start + len - 1
                in_start,
                root_idx - 1,
            )
            root.right = helper(
                pre_start
                + left_len
                + 1,  # start of the preorder right is the end of preorder left + 1
                pre_end,
                root_idx + 1,
                in_end,
            )
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
