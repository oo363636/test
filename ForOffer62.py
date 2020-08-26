"""0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，
因此最后剩下的数字是3
"""


class Solution:

    def last_remaining(self, n: int, m: int) -> int:
        """f(n, m) = 0  n = 1
            f(n, m) = [f(n-1, m) + m ] % n
            约瑟夫环问题
        """
        pos = 0
        for i in range(2, n + 1):
            pos = (pos + m) % i
        return pos


if __name__ == '__main__':
    test = Solution()
    a = test.last_remaining(10, 17)
    print(a)
