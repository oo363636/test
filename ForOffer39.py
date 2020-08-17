"""数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字
你可以假设数组是非空的，并且给定的数组总是存在多数元素"""


class Solution:

    def majority_element(self, nums: [int]) -> int:
        """摩尔投票法
        因为这里说明了众数超过数组长度的一半，所以遍历数组，当count为0的时候假设该数为众数x，当后
        一个数等于x时加1，如果不等则减1，当count为0的时候重新设置众数x
        最终得到的x一定为众数"""

        count = 0
        for num in nums:
            if count == 0:
                x = num
            num += 1 if num == x else -1
        return x


if __name__ == '__main__':
    test = Solution()
    c = test.majority_element([1, 2, 3, 2, 2, 2, 5, 4, 2])
    d = test.majority_element([3, 2, 3])
    print(c)  # 2
    print(d)  # 3