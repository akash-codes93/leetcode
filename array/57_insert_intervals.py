"""
https://leetcode.com/problems/insert-interval/?envType=list&envId=r5h55h9j
"""


class Solution:
    def insert(self, intervals, newInterval):

        my_st, my_en = newInterval
        new_int = []
        done = False

        for st, en in intervals:
            if my_en < st:
                if done is False:
                    new_int.append([my_st, my_en])
                    done = True

                new_int.append([st, en])

            elif st <= my_en <= en or st <= my_st <= en:
                my_st = min(st, my_st)
                my_en = max(en, my_en)

            elif my_st > en:
                new_int.append([st, en])

        if done is False:
            new_int.append([my_st, my_en])

        return new_int



