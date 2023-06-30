import bisect


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

            idx = bisect.bisect_right(endtimes, st-1) - 1    # not very happy with st-1 [question on geek]

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

