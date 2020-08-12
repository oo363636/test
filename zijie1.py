"""给一整数数组, 用当前元素之后数组中的最大元素来替换当前元素(右侧的最大元素).
因为最后一个元素的右边没有元素了, 所以用 -1 来替换这个值. 举个例子, 如果数组为 [16,17,4,3,5,2],
那么它就需要修改为 [17,5,5,5,2,-1]。 要求：你需要在原地实现（不允许创建新的数组或几何对象）。
样例： 
给出数组 nums = [16,17,4,3,5,2], 改变数组为 [17,5,5,5,2,-1]。
注意编程风格。（比较关注这个，我们认为这和你工作中代码质量有较强关联）
"""


class Solution:

    def replace_rbig(self, nums: [int]) -> [int]:
        # for i in range(1, len(nums)):
        #     rb = max(nums[i::])
        #     nums[i - 1] = rb
        # nums[len(nums) - 1] = -1
        # return nums

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                res = nums[i]
                nums[i] = -1
                continue
            res_temp = nums[i]
            nums[i] = res if res > nums[i + 1] else nums[i + 1]
            res = res_temp if res_temp > nums[i] else nums[i]
        return nums


if __name__ == '__main__':
    test = Solution()
    print(test.replace_rbig([16, 17, 4, 3, 5, 2]))
    print(test.replace_rbig([16, 1, 4, 8, 3, 2]))
