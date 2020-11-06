"""给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000"""


class Solution:

    def longestPalindrome(self, s: str) -> str:

        # dp算法，画一个二维表格True和False
        # size = len(s)
        #
        # max_len = 1
        # start = 0
        #
        # if size < 2:
        #     return s
        #
        # dp = [[False for _ in range(size)] for _ in range(size)]
        #
        # for i in range(size):
        #     dp[i][i] = True
        #
        # for j in range(1, size):
        #     for i in range(0, j):
        #
        #         if s[i] == s[j]:
        #             if j - i < 3:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i+1][j-1]
        #         else:
        #             dp[i][j] = False
        #
        #         if dp[i][j]:
        #             cur_len = j - i + 1
        #             if cur_len > max_len:
        #                 max_len = cur_len
        #                 start = i
        #
        # return s[start: start + max_len]

        # 中心扩散法，时间O（N方），空间O（1），比dp更快
        size = len(s)

        if size < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(size):

            palindrome_odd, len_odd = self.center(s, size, i, i)
            palindrome_even, len_even = self.center(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if len_odd >= len_even else palindrome_even

            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def center(self, s, size, left, right):

        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i + 1: j], j - i - 1


test = Solution()
a = test.longestPalindrome('ccc')
print(a)