

import bisect


class Solution:
    def maxEnvelopes(self, envelopes) -> int:

        s_env = list(sorted(envelopes, key=lambda x: (x[0], -x[1])))

        # area = [i[0]*i[1]for i in s_env]
        # print(area)
        max_len = 0
        dp = []

        for i in range(len(s_env)):
            h = s_env[i][1]

            idx = bisect.bisect_left(dp, h)

            # dp [], val 1 : idx => 0
            if len(dp) == idx:
                dp.append(h)
            else:
                dp[idx] = h

            if len(dp) > max_len:
                max_len = len(dp)

        # print(dp)
        return max_len
