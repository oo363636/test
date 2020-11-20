"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
"""


class Solution:

    def trap(self, height: [int]) -> int:

        # 1
        # 按列来求，左右分别寻找最高，两个最高的小者跟第i列的高度相减，就是能填充雨水的地方
        # 但是时间复杂度较高，O（N2），空间O（1）
        # total = 0
        #
        # for i in range(len(height)):
        #     left = 0
        #     right = 0
        #
        #     for j in range(i, -1, -1):
        #         if height[j] > left:
        #             left = height[j]
        #
        #     for j in range(i, len(height)):
        #         if height[j] > right:
        #             right = height[j]
        #
        #     if min(left, right) <= height[i]:
        #         continue
        #     else:
        #         total += min(left, right) - height[i]
        #
        # return total

        # 2
        # dp，找左右两边最高的，然后存进两个数组里，用空间换时间，空间O（N），时间O（N）
        left = [0] * len(height)
        right = [0] * len(height)
        total = 0
        for i in range(1, len(height) - 1):
            left[i] = max(left[i - 1], height[i - 1])

        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        for i in range(len(height)):
            # if min(left[i], right[i]) <= height[i]:
            #     continue
            # else:
            #     total += min(left[i], right[i]) - height[i]
            if min(left[i], right[i]) > height[i]:
                total += min(left[i], right[i]) - height[i]

        return total


test = Solution()
a = test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(a)

