class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, node_to_find, path, found):

            path.append(node)

            if found[0]:
                return

            if node == node_to_find:
                found[0] = True
                return

            if node.left and not found[0]:
                dfs(node.left, node_to_find, path, found)

            if node.right and not found[0]:
                dfs(node.right, node_to_find, path, found)

            if not found[0]:
                path.pop()

        path1 = []
        path2 = []
        dfs(root, p, path1, [False])
        dfs(root, q, path2, [False])

        p1, p2 = path1, path2
        # for i in p1:
        #     print(i.val, end="->")
        # print()
        # for i in p2:
        #     print(i.val, end="->")
        # print(p1, p2)

        common_path = []
        i = 0
        j = 0
        while i < len(p1) and j < len(p2):
            if p1[i] == p2[j]:
                common_path.append(p1[i])
                i += 1
                j += 1
            else:
                break
        # print(path)
        return common_path[-1]

