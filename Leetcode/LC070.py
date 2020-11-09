"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶?
给定 n 是一个正整数
"""


class Solution:
    @functools.lru_cache(100)  # 加缓存器，不然就超时了
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # if n == 1 or n == 2:
        #     return n
        # a, b, tmp = 1, 2, 0
        # for _ in range(3, n + 1):
        #     tmp = a + b
        #     a = b
        #     b = tmp

        # return tmp

test = Solution()
a = test.climbStairs(3)
print(a)