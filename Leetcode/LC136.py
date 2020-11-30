"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
from functools import reduce


class Solution:

    """
    任何数和 00 做异或运算，结果仍然是原来的数，即 a⊕0=a。
    任何数和其自身做异或运算，结果是 00，即 a⊕a=0。
    异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。
    因为有其他都是出现两次，比如有2m+1个数，那么2m个数异或出来得到的就是0，再异或最后这个单独的数就是我们所求
    """
    def singleNumber(self, nums: [int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


test = Solution()
a = test.singleNumber([1, 2, 1, 4, 2])
print(a)