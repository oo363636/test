"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头
"""


class Solution:

    def plusOne(self, digits: [int]) -> [int]:

        size = len(digits)

        for i in range(size-1, -1, -1):

            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits

        return [1] + digits  # 当所有都为0的时候，证明都是9，所以返回变成1000000（n个零）


test = Solution()
a = test.plusOne([0])
print(a)
