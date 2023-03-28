"""
@url: https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/

idea: In bfs when you see a NULL node post that all the nodes should be NULL



"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
            else:
                while queue:  # after finding the first NULL rest of the node should also be NULL
                    if queue.pop(0):
                        return False

        return True


_root = TreeNode(1
                 ,
                 TreeNode(2,
                          TreeNode(4, TreeNode(8)), TreeNode(5)
                          ),
                 TreeNode(3,
                          # TreeNode(6), TreeNode(7)
                          )
                 )

ans = Solution().isCompleteTree(_root)
print(ans)
