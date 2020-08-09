"""写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1"""


class ForOffer1001:

    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    test = ForOffer1001()
    print(test.fib(3))

"""
最好不要用f(n) = f(n-1) + f(n-2),这样会大量的递归计算，会继续往下递归
"""
