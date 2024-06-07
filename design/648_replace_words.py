"""
https://leetcode.com/problems/replace-words/description/

dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
"""

from typing import List


class Node:

    def __init__(self, value, ends_here=False):
        self.value = value
        self.ends_here = ends_here
        self.next_nodes = [None] * 26


class Trie:

    def __init__(self):
        self.base = Node('/')
    
    def insert(self, value):
        tr = self.base
        i = 0
        while i < len(value):
            idx = ord(value[i]) - 97
            
            if tr.next_nodes[idx] == None:
                node = Node(value[i])
            else:
                node = tr.next_nodes[idx]
            
            tr.next_nodes[idx] = node
            if i == len(value) - 1:
                node.ends_here = True
            
            tr = node
            i += 1

    def get_prefix(self, value):
        tr = self.base
        i = 0
        
        while i < len(value):
            idx = ord(value[i]) - 97
            
            if tr.next_nodes[idx] != None:
               node = tr.next_nodes[idx]
            else:
                break
            
            if node.ends_here == True:
                return value[:i+1]
            i += 1
            tr = node
        
        return value

    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        new_sentence = []
        for word in sentence.split(' '):
            print(trie.get_prefix(word))
            new_sentence.append(trie.get_prefix(word))
        return " ".join(new_sentence)
        


print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
