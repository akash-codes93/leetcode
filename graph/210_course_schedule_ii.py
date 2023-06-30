"""
https://leetcode.com/problems/course-schedule-ii/
"""

from collections import defaultdict


class Solution:

    def findOrder(self, numCourses: int, prerequisites):

        def task_order(prerequisite, n):
            eout = defaultdict(set)
            ein = defaultdict(set)

            def link(_from, to):
                eout[_from].add(to)
                ein[to].add(_from)

            def unlink(_from, to):
                eout[_from].remove(to)
                ein[to].remove(_from )

            outDegZero = lambda x: len(eout[x]) == 0

            for to, _from in prerequisite:
                link(_from, to)

            queue = list(filter(outDegZero, [i for i in range(n)]))
            # print("base queue:", queue)
            task_order = []
            while queue:
                # print(queue)
                node = queue.pop(0)
                task_order.append(node)

                for inward in tuple(ein[node]):
                    unlink(inward, node)
                    if outDegZero(inward):
                        queue.append(inward)

            task_order.reverse()
            return task_order
        t = task_order(prerequisites, numCourses)
        return [] if len(t) != numCourses else t

