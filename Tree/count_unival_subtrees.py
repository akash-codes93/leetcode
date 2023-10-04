"""
solved from coding ninjas,
premium question on leetcode
"""
import queue
import sys

sys.setrecursionlimit(10 ** 6)


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def countUnivalTrees(_root):
    # Write your code here.
    # This function returns the updated root.
    total_trees = [0]

    def dfs(root):
        if root is None:
            return  True

        left = dfs(root.left)
        right = dfs(root.right)

        if left and right:
            if root.left is None and root.right is None:
                total_trees[0] += 1
                return True
            elif root.left is None and root.right is not None:
                if root.right.data == root.data:
                    total_trees[0] += 1
                    return True
            elif root.left is not None and root.right is None:
                if root.left.data == root.data:
                    total_trees[0] += 1
                    return True
            elif root.left.data == root.right.data == root.data:
                    total_trees[0] += 1
                    return True

        return False

    dfs(_root)
    return total_trees[0]



def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)

    if length <= 0 or levelorder[0] == -1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


t = int(input())
while t > 0:
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(countUnivalTrees(root))
    t = t - 1

