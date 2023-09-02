class Solution:
    def snakesAndLadders(self, board) -> int:
        mapper = {}
        i = 1
        dir = 1
        n = len(board)

        while board:
            row = board.pop()

            while row:
                if dir == 1:
                    val = row.pop(0)
                else:
                    val = row.pop()

                if val == -1:
                    i += 1
                else:
                    mapper[i] = val
                    i += 1
            dir = dir * -1

        print(mapper)
        queue = [(1, 0)]
        visited = set({1})

        while queue:
            pos, dest = queue.pop(0)

            if pos == n * n:
                return dest

            dest = dest + 1

            # if pos in mapper:# and mapper[pos] not in visited:
            #     queue.append((mapper[pos], dest))
            #     visited.add(mapper[pos])

            for i in range(1, 7):
                if (pos + i) > n * n:
                    continue
                # if (pos + i) in visited: continue
                next_pos = mapper[(pos + i)] if (pos + i) in mapper else (pos + i)

                if next_pos not in visited:
                    queue.append((next_pos, dest))
                    visited.add(next_pos)

        return -1
