class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def constructFromPrePost(self, preorder, postorder):

        # predict = {val: idx for idx, val in enumerate(preorder)}
        postdict = {val: idx for idx, val in enumerate(postorder)}

        def dfs(prestart, preend, poststart, postend):
            if prestart == preend:
                return TreeNode(preorder[prestart])
            if prestart > preend:
                return None

            root_val = preorder[prestart]
            node = TreeNode(root_val)

            next_root = preorder[prestart + 1]
            next_root_post = postdict[next_root]

            left_count = next_root_post - poststart

            node.right = dfs(prestart+1, prestart+1+left_count, poststart, next_root_post)

            node.left = dfs(prestart+1+left_count+1, preend,next_root_post+1, postend-1 )

            return node

        return dfs(0, len(preorder)-1, 0, len(postorder)-1)


# def solution1(s):
#     if len(s) == len(set(s)):
#         return s
#
#     stack = []
#     for i in s:
#         popped = False
#         while stack and stack[-1] == i:
#             c = stack.pop()
#             stack.append(chr(ord(c) + 1))
#             popped = True
#
#         if not popped:
#             stack.append(i)
#     s1 = ""
#     while stack:
#         s1 += stack.pop()
#     # print(s[::-1])
#     return solution(s1[::-1])


# print(solution("a" * 100))

# '11 11 11 11 11 1'

# 11 % 2 == 1

# " 2 2 2 2 2 1"
# " 22 22 2"
# "3 3"

# 5 % 2 = 1

# "zz zz"
#
# "aaaaaaaaaa"
# 11

# def solution(n):
#
#     initial = 97
#     s = ""
#     while n:
#         if n % 2 != 0 or initial == 122:
#             s += chr(initial)
#
#         n = n//2
#         if initial < 122:
#             initial += 1
#
#     return s[::-1]


# print(solution(1000000000))
# print(solution(67108876))
# print(solution(11))
# print(solution(1))



