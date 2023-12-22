import bisect
import heapq


class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here

        meetings = [[start[i], end[i]] for i in range(len(start))]
        meetings = sorted(meetings, key=lambda x: x[1])

        endtimes = [i[1] for i in meetings]

        dp = [1] * len(meetings)

        for i in range(1, len(meetings)):
            st = meetings[i][0]
            en = meetings[i][1]

            idx = bisect.bisect_right(endtimes, st - 1) - 1  # not very happy with st-1 [question on geek]

            dp[i] = max(dp[i - 1], (dp[idx] + 1 if idx >= 0 else 1))

        print(dp)
        return max(dp)


Solution().maximumMeetings(
    47,
    [86, 32, 31, 98, 37, 65, 98, 71, 99, 58, 59, 32, 52, 69, 15, 75, 4, 86, 57, 36, 83, 18, 58, 50, 43, 29, 98, 53, 80,
     5, 89, 73, 8, 97, 17, 100, 9, 21, 55, 55, 32, 74, 60, 32, 87, 72, 54],
    [126, 112, 134, 138, 89, 118, 107, 124, 126, 83, 133, 64, 124, 109, 108, 132, 111, 95, 82, 106, 86, 118, 82, 78, 92,
     55, 128, 121, 118, 95, 94, 110, 111, 146, 124, 148, 95, 146, 109, 61, 93, 126, 74, 76, 110, 78, 91]
)

"""
meetings rooms II
minimum rooms required to conduct all meetings
"""


def meeting_rooms(meetings):
    meetings = sorted(meetings, key=lambda x: x[1])
    end_times = [i[1] for i in meetings]

    dp = [1] * len(meetings)

    for i in range(1, len(meetings)):
        st = meetings[i][0]
        en = meetings[i][1]

        idx = bisect.bisect_right(end_times, st) - 1

        dp[i] = 0 if idx >= 0 else 1
        del end_times[idx]

    print(sum(dp))
    return sum(dp)


def min_meeting_rooms(meetings) -> int:
    # Write your code here

    meetings = sorted(meetings, key=lambda x: x.start)
    heap = [meetings[0].end]
    max_meetings = 1

    for meeting in meetings[1:]:
        while heap and heap[0] <= meeting.start:
            heapq.heappop(heap)
        heapq.heappush(heap, meeting.end)
        max_meetings = max(max_meetings, len(heap))

    return max_meetings


# meeting_rooms([(30, 75), (0, 50), (60, 150)])
# min_meeting_rooms([(30, 75), (0, 50), (60, 150)])
# min_meeting_rooms([(1, 18), (18, 23), (15, 29), (5, 14), (2, 11), (5, 13)])

# 8904242424


import sys

ENTER = "enter"
EXIT = "exit"


def get_busiest_slot(events):
    ts_entries, ts_exits = dict(), dict()
    max_time, min_time = -sys.maxsize, sys.maxsize

    for event in events:
        ts_dict = None
        timestamp = event["timestamp"]
        if event["type"] == ENTER:
            ts_dict = ts_entries
        else:
            ts_dict = ts_exits

        ts_dict[timestamp] = event["count"]
        if timestamp < min_time:
            min_time = timestamp
        elif timestamp > max_time:
            max_time = timestamp

    people_inside = 0
    max_people_inside = 0
    start_time, end_time = None, None
    for timestamp in range(min_time, max_time + 1):
        if timestamp in ts_entries:
            people_inside += ts_entries[timestamp]
            if people_inside > max_people_inside:
                max_people_inside = people_inside
                start_time = timestamp
        if timestamp in ts_exits:
            if people_inside == max_people_inside:
                end_time = timestamp
            people_inside -= ts_exits[timestamp]

    return (start_time, end_time)


def simple_sort_solution(events):

    count = 0
    start_time = None
    end_time = None
    max_people = 0

    for event in events:
        if event["type"] == "enter":
            count += event["count"]
            if count > max_people:
                start_time = event["timestamp"]
                max_people = count
        else:
            if count == max_people:
                end_time = event["timestamp"]
            count -= event["count"]

    return (start_time, end_time)





y=simple_sort_solution([{"timestamp": 1, "count": 10, "type": "enter"},
{"timestamp": 3, "count": 2, "type": "exit"},
{"timestamp": 5, "count": 1, "type": "enter"},
{"timestamp": 6, "count": 1, "type": "enter"},
{"timestamp": 7, "count": 1, "type": "enter"},
{"timestamp": 9, "count": 3, "type": "exit"},
{"timestamp": 10, "count": 8, "type": "exit"}])
print(y)


def consecutive_ones(n):

    max_count = 0
    count = 0

    while n > 0:
        print(n, n & 1)
        if n & 1 == 1:
            count += 1
        else:
            count = 0

        print(count)
        max_count = max(count, max_count)
        print(max_count)

        n >>= 1

    return max_count


print("Ans: ", consecutive_ones(156))
print("Ans: ", consecutive_ones(3))
