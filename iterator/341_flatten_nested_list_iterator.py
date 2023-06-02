# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class Node:

    def __init__(self, idx, _list):
        self.idx = idx
        self.list = _list


class NestedIterator:

    def __init__(self, nestedList):

        self.stack = []
        if nestedList.getInteger():
            self.stack.append(Node(0, nestedList))

    def next(self) -> int:
        node = self.stack.pop()

        if type(node.list[node.idx]) == int:
            out = node.list[node.idx]
            node.idx += 1
            if node.idx < len(node.list):
                self.stack.append(node)
            return out
        else:
            new_list = node.list[node.idx]
            node.idx += 1
            if node.idx < len(node.list):
                self.stack.append(node)
            if len(new_list) > 0:
                new_node = Node(0, new_list)
                self.stack.append(new_node)
            else:
                return
            return self.next()

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False


# itera = NestedIterator([0, [[[1],2,3],4,5,6]])
# itera = NestedIterator([1,2,3,4,5,[6]])
# itera = NestedIterator([[1,1],2,[1,1]])
itera = NestedIterator([[]])

while itera.hasNext():
    print(itera.next())


"""
[1,2,3,4,5]
[0, [[[1],2,3],4,5,6]]
[[1,1],2,[1,1]]
[[]]
[0]
"""
