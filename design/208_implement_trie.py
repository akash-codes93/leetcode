class Node:

    def __init__(self, val, c=1, ends_here=False):
        self.val = val
        self.c = c
        self.ends_here = ends_here
        self.next_chars = [None] * 26


class Trie:

    def __init__(self):
        self.base_node = Node(val='/')

    def insert(self, word: str) -> None:
        i = 0
        tr = self.base_node
        while i < len(word):
            idx = ord(word[i]) - 97
            if tr.next_chars[idx] is None:
                node = Node(word[i], 1, False)
                tr.next_chars[idx] = node
            else:
                node = tr.next_chars[idx]
                node.c += 1

            if i == len(word) - 1:
                node.ends_here = True

            tr = node
            i += 1

    def search(self, word: str) -> bool:
        tr = self.base_node
        i = 0
        while i < len(word):
            idx = ord(word[i]) - 97
            # print(idx)
            if tr.next_chars[idx] is None:
                return False
            else:
                tr = tr.next_chars[idx]
                i += 1

        if tr.ends_here:
            return True
        return False

    def startsWith(self, word: str) -> bool:
        tr = self.base_node
        i = 0
        while i < len(word):
            idx = ord(word[i]) - 97
            if tr.next_chars[idx] is None:
                return False
            else:
                tr = tr.next_chars[idx]
                i += 1

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
