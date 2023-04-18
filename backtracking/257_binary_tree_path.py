"""
https://leetcode.com/problems/binary-tree-paths/

append only at leave. hence check for leaf is required.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):

        path = []

        def helper(root, sub_paths):
            if root == None:
                return

            sub_paths.append(str(root.val))

            helper(root.left, sub_paths)
            helper(root.right, sub_paths)

            if root.left is None and root.right is None:
                path.append("->".join(sub_paths))
            sub_paths.pop()

        helper(root, [])
        return path


_root = TreeNode(1
                 ,
                 TreeNode(2,
                          TreeNode(4, TreeNode(8)), TreeNode(5)
                          ),
                 TreeNode(3, TreeNode(8)
                          #      # ,Node(6), Node(7)
                          )
                 )



p = Solution().binaryTreePaths(_root)

print(p)