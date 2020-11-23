"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"
"""


class Solution:

    def convert(self, s: str, numRows: int) -> str:

        if numRows < 2:
            return s

        res = ['' for _ in range(numRows)]
        flag = -1
        k = 0
        for c in s:
            res[k] += c
            if k == 0 or k == numRows - 1:
                flag = -flag
            k += flag
        return ''.join(res)


test = Solution()
a = test.convert('LEETCODEISHIRING', 3)
print(a)
