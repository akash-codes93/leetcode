"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
calculate total length of words and extract substring of that length
in each substring extract words of size words[0] check if they exists and frequency array and frequency is also same.

"""
import copy
from collections import defaultdict, Counter


class Solution:

    def findSubstring(self, s: str, words):

        freq = Counter(words)

        word_len = len(words[0])
        total_len = word_len * len(words)
        output = []

        for i in range(0, (len(s) - total_len) + 1):

            temp_freq = copy.copy(freq)
            segment = s[i: i + total_len]
            # print(segment)
            for j in range(0, len(segment), word_len):
                sub_segment = segment[j: j+word_len]
                # print(sub_segment)
                if sub_segment not in temp_freq:
                    break
                else:
                    temp_freq[sub_segment] -= 1
                    if temp_freq[sub_segment] == 0:
                        temp_freq.pop(sub_segment)

            if len(temp_freq) ==0:
                output.append(i)

        return output


# ans = Solution().findSubstring("booooooo", ["ooo", "ooo"])
# ans = Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
ans = Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
print(ans)
