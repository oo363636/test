"""给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。"""


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:

            if x > 0:
                pos = x % 10
            else:
                pos = x % -10  # 要除以-10才能得到想要的，因为python // 有向下取整的操作

            if rev > int(2147483647 / 10) or (rev == int(2147483647 // 10) and pos > 7):
                return 0
            if rev < int(-2147483648 / 10) or (rev == int(-2147483648 / 10) and pos < -8):
                return 0
            rev = rev * 10 + pos
            x = int(x / 10)
        return rev

    """
    题解提供的另一个方法。
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res
    """


test = Solution()
a = test.reverse(-123)
print(a)
