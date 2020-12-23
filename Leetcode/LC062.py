"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
"""

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        # if m == 1 or n == 1:
        #     return 1
        #
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        #
        # dp[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             continue
        #         elif i == 0:
        #             dp[i][j] = dp[i][j-1]
        #         elif j == 0:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[m-1][n-1]

        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

        # 还有可以用组合数学的方法。需要移动 m+n-2次，其中有 m-1次向下移动，n-1次向右移动。
        # 因此路径的总数，就等于从 m+n-2次移动中选择 m-1次向下移动的方案数，即组合数：m-1 C m+n-2


test = Solution()
a = test.uniquePaths(3, 7)  # 28
print(a)