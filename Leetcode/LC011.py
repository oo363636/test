"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器
"""


class Solution:

    def maxArea(self, height: [int]) -> int:

        # 超时了！！！放弃！！！
        # num = len(height)
        # max_con = 0
        # for i in range(num - 1):
        #     for j in range(i, num):
        #         container = min(height[i], height[j]) * (j - i)
        #         if container > max_con:
        #             max_con = container
        # return max_con

        # 双指针法，求出当前双指针对应的容器的容量；
        # 对应数字较小的那个指针以后不可能作为容器的边界了，将其丢弃，并移动对应的指针。
        # 时间复杂度O（N）
        num = len(height)
        i = 0
        j = num - 1
        max_container = 0
        while i < j:
            container = min(height[i], height[j]) * (j - i)
            if container > max_container:
                max_container = container
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_container


test = Solution()
a = test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(a)  # 49
