"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案
"""


import collections

class Solution:

    def minWindow(self, s: str, t: str) -> str:

        # dic = dict()

        dic = collections.defaultdict(int)
        i = 0

        for c in t:
            dic[c] += 1

        # for k in range(len(t)):
        #     if t[k] not in dic:
        #         dic[t[k]] = 1
        #     else:
        #         dic[t[k]] += 1

        need_count = len(t)

        res = (0, float('inf'))

        for j, c in enumerate(s):
            if dic[c] > 0:
                need_count -= 1
            dic[c] -= 1

            if need_count == 0:
                while True:
                    c = s[i]
                    if dic[c] == 0:
                        break
                    dic[c] += 1
                    i += 1

                if j-i < res[1] - res[0]:  # 记录结果
                    res = (i, j)

                dic[s[i]] += 1
                need_count += 1
                i += 1

        return '' if res[1] > len(s) else s[res[0]: res[1] + 1]


test = Solution()
a = test.minWindow('ADOBECODEBANC', 'ABC')
print(a)  # BANC