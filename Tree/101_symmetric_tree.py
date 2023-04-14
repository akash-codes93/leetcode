"""
@url: https://leetcode.com/problems/symmetric-tree/

 # fundamental applying bfs on tree very important
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def check_palindrome(self, queue):
        i = 0
        j = len(queue) - 1
        while i < j:
            if queue[i] is None and queue[j] is None:
                i += 1
                j -= 1
                continue

            elif queue[i] is None and queue[j] is not None:
                return False

            elif queue[i] is not None and queue[j] is None:
                return False

            elif queue[i].val != queue[j].val:
                return False
            i += 1
            j -= 1
        return True

    def check_queue_has_node(self, queue):
        for i in queue:
            if i is not None:
                return True

        return False

    def isSymmetric_bfs(self, root: Optional[TreeNode]) -> bool:
        # bfs approach
        queue = [root]
        next_queue = []

        while queue:

            node = queue.pop(0)
            if node:
                next_queue.append(node.left)
                next_queue.append(node.right)

            if len(queue) == 0:
                # check if next level is symmetric

                if not self.check_palindrome(next_queue):
                    return False

                queue = next_queue
                next_queue = []

                if not self.check_queue_has_node(queue):
                    return True

        return True

    def symmetric(self, left, right):
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is not None and right is not None and left.val != right.val:
            return False

        if left is None and right is None:
            return True

        return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # bfs approach
        if root is None:
            return True

        return self.symmetric(root.left, root.right)


# def create_tree_using_array(array):


_root = TreeNode(1,
                 TreeNode(2,
                          TreeNode(3), TreeNode(4)),
                 TreeNode(2,
                          TreeNode(4), TreeNode(3)),
                 )

resp = Solution().isSymmetric(_root)
print(resp)
