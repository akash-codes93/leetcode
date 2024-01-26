"""
https://leetcode.com/problems/palindrome-partitioning/description/


"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        mem = {}
        def dfs(suffix):
            if not suffix:
                return []

            if suffix in mem:
                print("mem used")
                return mem[suffix]

            partitions = []
            if suffix == suffix[::-1]:
                partitions.append([suffix])

            for i in range(1, len(suffix)):
                word = suffix[:i]
                if word != word[::-1]:
                    continue

                subpartitions = dfs(suffix[i:])
                for subpartition in subpartitions:
                    partitions.append([word] + subpartition)

            mem[suffix] = partitions
            return mem[suffix]

        return dfs(s)


