from typing import (
    List,
)

from collections import defaultdict
from itertools import chain


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        eout = defaultdict(set)
        ein = defaultdict(set)

        def link(_from, to):
            eout[_from].add(to)
            ein[to].add(_from)

        def unlink(_from, to):
            eout[_from].remove(to)
            ein[to].remove(_from)

        chars = set()

        for i in range(1, len(words)):
            first_word = words[i-1]
            second_word = words[i]

            min_len = max(len(first_word), len(second_word))
            s = 0
            for j in range(min_len):

                if j < len(first_word) and j < len(second_word):
                    a = first_word[j]
                    b = second_word[j]

                    if a != b and s != 1:
                        s = 1
                        link(a, b)

                if j < len(first_word):
                    chars.add(first_word[j])

                if j < len(second_word):
                    chars.add(second_word[j])

        queue = []
        out_deg_zero = lambda x: len(eout[x]) == 0

        for each_char in ein:
            print(each_char)
            if out_deg_zero(each_char):
                queue.append(each_char)
                chars.remove(each_char)

        print(queue)
        order = ""
        while queue:
            char = queue.pop(0)
            order += char

            for each_char in tuple(ein[char]):
                unlink(each_char, char)
                if out_deg_zero(each_char):
                    queue.append(each_char)
                    chars.remove(each_char)

        def check_empty_dict():
            for key, val in eout.items():
                if len(val) != 0 :
                    return False
            return True

        if not check_empty_dict():
            return ""

        order = order[::-1]
        order = order + "".join(sorted(list(chars)))
        print(order)
        return order


# Solution().alien_order(["wrt","wrf","er","ett","rftt"])
# Solution().alien_order(["c", "adhkjsf"])
Solution().alien_order(["ab","adc"])












