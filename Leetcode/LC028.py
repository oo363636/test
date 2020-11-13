"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1
"""


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        # 最简单，但是不需要每个字符串都完全比较，第一个相等才比较下去
        # size_small = len(needle)
        # size_large = len(haystack)
        #
        # for i in range(size_small - 1, size_large):
        #     if haystack[i-size_small+1: i+1] == needle:
        #         return i - size_small + 1
        # return -1

        # 匹配第一个字符，不相等则往后，相等再继续匹配
        L = len(needle)
        n = len(haystack)

        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            cur_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                cur_len += 1

            if cur_len == L:
                return pn - L

            pn = pn - cur_len + 1

        return -1


test = Solution()
a = test.strStr('abddcc', 'dc')
print(a)