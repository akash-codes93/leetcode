class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        l = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                l.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                l.append(None)

        s = ""
        for i in l:
            s += str(i) + ","
        print(s)
        return s[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')

        head_val = l.pop(0)
        if head_val:
            head = TreeNode(head_val)
            nodes = [head]
        else:
            head = head_val

        while l:
            node = nodes.pop(0)
            i = l.pop(0)
            if i:
                node.left = TreeNode(i)
            else:
                node.left = i

            i = l.pop(0)
            if i:
                node.right = TreeNode(i)
            else:
                node.right = i

            if node.left:
                nodes.append(node.left)

            if node.right:
                nodes.append(node.right)

        return head


root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4), TreeNode(5)),
                TreeNode(3,
                         TreeNode(6), TreeNode(7))
                )

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ans.val)
print(ans.left.val)
print(ans.right.val)
print(ans.left.left.val)
print(ans.left.right.val)
print(ans.right.left.val)
print(ans.right.right.val)
print(ans.right.right.right.val)