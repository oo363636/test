"""一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字
"""


class Solution:

    def missing_number(self, nums: [int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:  # num[m] != m
                j = m - 1
        return i  # 返回的是索引，缺失的元素等于右子数组的首位元素


if __name__ == '__main__':
    test = Solution()
    # a = test.missing_number([0, 2, 3, 4])
    # print(a)
    b = test.missing_number([0, 1, 2, 3, 5, 6, 7])
    print(b)  # 4