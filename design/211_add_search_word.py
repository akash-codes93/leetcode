"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class TrieNode:

    def __init__(self, val, ends_here=False):
        self.val = val
        self.ends_here = ends_here
        self.next_chars = [None]*26


class WordDictionary:

    def __init__(self):

        self.base = TrieNode('/')

    def addWord(self, word: str) -> None:
        tr = self.base
        i = 0

        while i < len(word):
            idx = ord(word[i]) - 97

            if tr.next_chars[idx] is None:
                node = TrieNode(word[i])
                tr.next_chars[idx] = node
            else:
                node = tr.next_chars[idx]

            if i == (len(word)-1):
                node.ends_here = True

            tr = node
            i += 1

    def search(self, word: str) -> bool:

        def dfs(tr, i):

            if i == (len(word)):
                if tr.ends_here == True:
                    return True
                return False

            if word[i] == '.':
                for j in range(0, 26):
                    if tr.next_chars[j] != None and dfs(tr.next_chars[j], i+1):
                        return True
            else:
                idx = ord(word[i]) - 97
                if tr.next_chars[idx] != None and dfs(tr.next_chars[idx], i+1):
                    return True

            return False

        return dfs(self.base, 0)
