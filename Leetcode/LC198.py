"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，
系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额
"""


class Solution:

    def rob(self, nums: [int]) -> int:

        # 动态规划，两个选择，要么偷，要么不偷
        # 偷的话，i-1不能偷，所以是i-2的state加上当前的金额
        # 不偷的话，就等于i-1的state
        # 两者最大值即为当前state
        length = len(nums)
        state = [0] * length

        if length == 0:
            return 0

        if length == 1:
            return nums[0]

        # state[0] = nums[0]
        # state[1] = max(nums[0], nums[1])

        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, length):
            tmp = second
            second = max(first + nums[i], second)
            first = tmp

        return second

            # state[i] = max(state[i-1], state[i-2] + nums[i])
        # return state[length-1]


test = Solution()
a = test.rob([1, 2, 3, 1])
print(a)
