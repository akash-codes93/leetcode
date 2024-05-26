"""
https://leetcode.com/problems/word-break-ii/description/?envType=daily-question&envId=2024-05-25
"""
from typing import List


class Node:
    def __init__(self, val, ends_here=False):
        self.val = val
        self.ends_here = ends_here
        self.next_chars = [None] * 26


class Trie:

    def __init__(self):
        self.base_node = Node('/')

    def insert(self, word):
        tr = self.base_node
        i = 0
        while i < len(word):
            idx = ord(word[i]) - 97
            if tr.next_chars[idx] is None:
                node = Node(word[i])
                tr.next_chars[idx] = node
            else:
                node = tr.next_chars[idx]

            if i == len(word) - 1:
                node.ends_here = True

            tr = node
            i = i + 1

    def search(self, word):
        tr = self.base_node
        i = 0
        while i < len(word):
            idx = ord(word[i]) - 97
            if tr.next_chars[idx] is None:
                return False

            tr = tr.next_chars[idx]
            i += 1

        if tr.ends_here == True:
            return True
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        trie = Trie()
        # wordDict = set(wordDict)
        for word in wordDict:
            trie.insert(word)

        mem = {}

        def dfs(suffix):
            if suffix in mem:
                return mem[suffix]

            if len(suffix) == 0:
                return []

            result = []
            for i in range(1, len(suffix) + 1):
                left = suffix[: i]
                rem = suffix[i:]
                if trie.search(left):
                    right = dfs(rem)

                    if len(right) > 0:
                        for r in right:
                            result.append(left + " " + r)
                    else:
                        result.append(left)
            mem[suffix] = result
            return result

        return dfs(s)
