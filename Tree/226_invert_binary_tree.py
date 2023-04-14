"""
@url: https://leetcode.com/problems/invert-binary-tree/description/

do look tree as whole just look at the node and how to recusively do it for children

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root

        temp = root.left
        root.left = temp
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


