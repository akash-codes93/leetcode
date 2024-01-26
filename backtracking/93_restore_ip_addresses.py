"""
https://leetcode.com/problems/restore-ip-addresses/
"""


class Solution:
    def restoreIpAddresses(self, s: str):
        main_output = []

        def dfs(s, ip, dots):
            print(s, ip, dots)
            if s == "":
                if dots == -1:
                    main_output.append(ip)
                return

            if dots == -1 and len(s) > 0:
                return

            for i in range(len(s) - 1, max(-1, len(s) - 4), -1):
                subnet = s[i:]

                if len(subnet) == 2 and subnet[0] == '0':
                    continue

                elif len(subnet) == 3 and (subnet[0] == '0' or int(subnet) > 255):
                    continue
                if ip == "":
                    dfs(s[:i], subnet, dots - 1)
                else:
                    dfs(s[:i], subnet + '.' + ip, dots - 1)

        dfs(s, "", dots=3)
        return main_output


o = Solution().restoreIpAddresses("101023")
print(o)
