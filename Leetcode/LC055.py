"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置
"""


class Solution:

    def canJump(self, nums: [int]) -> bool:

        # 贪心算法
        # 我们依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置。对于当前遍历到的位置 x，
        # 如果它在 最远可以到达的位置 的范围内，那么我们就可以从起点通过若干次跳跃到达该位置，
        # 因此我们可以用 x + nums[x] 更新 最远可以到达的位置

        # 如果 最远可以到达的位置 大于等于数组中的最后一个位置，那就说明最后一个位置可达，我们就可以直接返回 True 作为答案
        distance = 0

        for i in range(len(nums)):
            if i <= distance:
                distance = max(nums[i] + i, distance)
                if distance >= len(nums) - 1:
                    return True

        return False


test = Solution()
a = test.canJump([3, 2, 1, 0, 4])
print(a)