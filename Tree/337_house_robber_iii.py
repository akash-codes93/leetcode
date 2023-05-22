"""
https://leetcode.com/problems/house-robber-iii/description/

1.) bottom up traversal
2.) include & exclude a node
3.) [0,0] if node does not exists
4.) line 25 all possible combinations if you don't take the current node

"""


class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return [0, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            # include
            inc = root.val + left[1] + right[1]

            # exclude
            exc = max((left[0] + right[0]), (left[1] + right[1]), (left[0] + right[1]), (left[1] + right[0]))

            return [inc, exc]

        return max(dfs(root))


from collections import OrderedDict