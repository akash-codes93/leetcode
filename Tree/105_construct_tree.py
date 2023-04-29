"""

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):

        inorder_hash = {}
        for i in range(0, len(inorder)):
            inorder_hash[inorder[i]] = i

        preorder_hash = {}
        for i in range(0, len(preorder)):
            preorder_hash[preorder[i]] = i

        print(inorder_hash, preorder_hash)

        def builder(pstart, pend, istart, iend):
            if pstart >= pend or istart >= iend:
                return None

            rootval = preorder[pstart]
            print("rootval: ", rootval)
            root_index = inorder_hash[rootval]
            print("root_index: ", root_index)

            values = root_index -istart
            print("values: ", values)


            root = TreeNode(rootval)
            root.left = builder(pstart+1, pstart+values, istart, root_index - 1)
            root.right = builder(pstart+values+1, pend, root_index + 1, iend)

            return root

        return builder(0, len(preorder) - 1, 0, len(inorder) - 1)


Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])