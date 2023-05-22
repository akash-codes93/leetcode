"""
https://leetcode.com/problems/iterator-for-combination/

using bits manipulation and backtracking
"""

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        self.string = characters
        self.length = combinationLength

        self.combinations = []

        # self.dfs("", 0, self.length)
        self.get_combinations()
        print(self.combinations)
        # self.combinations.sort()
        self.i = 0

    def dfs(self, s, i, available):
        # print(s,i, available)
        if i == len(self.string):
            if available == 0:
                # print(s)
                self.combinations.append(s)
            return

        for p in [1, 0]:
            if p:
                s += self.string[i]
                self.dfs(s, i + 1, available - 1)
                s = s[:-1]
            else:
                self.dfs(s, i + 1, available)
        return

    def get_combinations(self):
        for i in range(1 << len(self.string)):
            print("--")
            s = ""

            for j in range(0, len(self.string)):
                if i & (1 << j):
                    print(j)
                    s += self.string[j]

            if len(s) == self.length:
                print(s, i)
                self.combinations.append(s)

    def next(self) -> str:
        # print(self.combinations, self.i)
        p = self.combinations[self.i]
        self.i += 1
        return p

    def hasNext(self) -> bool:
        if self.i < len(self.combinations):
            return True
        return False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()