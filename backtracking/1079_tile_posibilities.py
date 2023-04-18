"""
https://leetcode.com/problems/letter-tile-possibilities/description/

idea: outer loop is for number of positions that is 1 to len(tiles)

inner loop is to start with start letter then check if it is not included in path.

draw the tree, very very useful, code will come automatically.

"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        main = set()

        def looper(pos, path):
            if pos == 0:
                k = [tiles[o] for o in path]
                main.add("".join(k))
                return

            for i in range(0, len(tiles)):
                if i not in path:
                    path.append(i)
                    looper(pos - 1, path)
                    path.pop()

        for p in range(1, len(tiles) + 1):
            looper(p, [])
        print(main)
        return len(main)


a = Solution().numTilePossibilities("ACB")
print(a)