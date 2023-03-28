"""
@url: https://leetcode.com/problems/diameter-of-binary-tree/description/


- height of a null tree is -1

- diameter D , Height H

H(node) = Height(left sub tree) + Height(right sub tree) + 1

D = H(Left sub tree) + H(Right sub tree) + 2

2 because lets suppose we have to find diameter of leaf node
which according to above formula will be

D[leaf node] = H[left null node] + H[right null node] + 2
             = -1 + -1 + 2

 Also, we need to traverse this bottom up
 reverse we will do the work twice for every node
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bottom-up approach
        max_diameter = [0]  # used as list because of global variable otherwise internal def does not recognise it.

        def dfs(root):
            if root is None:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            max_diameter[0] = max(max_diameter[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)

        return max_diameter[0]

    def height_bt(self, node):
        if node is None:
            return -1

        return max(self.height_bt(node.left), self.height_bt(node.right)) + 1

    def diameter_bt(self, root: Optional[TreeNode]) -> int:
        # top-down approach # bad because every node is traversed multiple times
        if root is None:
            return 0

        current_diameter = self.height_bt(root.left) + self.height_bt(root.right) + 2
        return max(current_diameter, self.diameter_bt(root.left), self.diameter_bt(root.right))


_root = TreeNode(1
                 ,
                 TreeNode(2,
                          TreeNode(4, TreeNode(8)), TreeNode(5)
                          ),
                 TreeNode(3
                          #      # ,Node(6), Node(7)
                          )
                 )

# p = Solution().longest_path_to_leaf(_root)
# p = Solution().diameterOfBinaryTree(_root)
# p = Solution().diameterOfBinaryTree(_root)
p = Solution().diameter_bt(_root)
print(p)
