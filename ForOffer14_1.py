"""给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


class ForOffer14_1:
    def cutting_rope(self, n: int) -> int:
        """使用动态规划dp"""
        dp = [0 for i in range(n+1)]
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j])  # dp[i]表示不剪切，j*dp[i-j]表示在j处剪切
        return dp[n]


if __name__ == '__main__':
    cr = ForOffer14_1()
    print(cr.cutting_rope(8))   # 18
