"""假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？"""

from typing import List


class ForOffer63:
    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        cost = float("inf")
        for i in range(len(prices)):
            cost = min(cost, prices[i])
            profit = max(profit, prices[i] - min(cost, prices[i]))
        return profit


if __name__ == '__main__':
    mp = ForOffer63()
    print(mp.max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(mp.max_profit([7, 6, 4, 3, 1]))  # 0


"""
    更优雅的方式：
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

"""