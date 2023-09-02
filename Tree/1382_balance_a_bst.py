"""

import concept of binary partition.
binary partition leads to balanced tree

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        def bp(l, r):
            if r < l: return

            mid = (l + r) // 2
            node = TreeNode(arr[mid])
            node.left = bp(l, mid - 1)
            node.right = bp(mid + 1, r)

            return node

        return bp(0, len(arr) - 1)
