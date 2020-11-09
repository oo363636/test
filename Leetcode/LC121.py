"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票
"""


class Solution:

    def maxProfit(self, prices: [int]) -> int:

        # 简化版本的动态规划，不需要空间O（n）的复杂度，仅仅存两个变量，O（1）即可
        # 最低点是我们想要的，找在后面的最高点减去这个最低点就是最大的利润
        max_profit = 0
        min_price = float('+inf')

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


test = Solution()
a = test.maxProfit([7, 1, 5, 3, 6, 4])  # 5
print(a)