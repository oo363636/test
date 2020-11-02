"""判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。"""


class Solution:

    def isPalindrome(self, x: int) -> bool:

        """
        tmp = x
        p = 0

        if tmp < 0:
            return False

        while tmp != 0:
            p = p * 10 + tmp % 10
            tmp //= 10

        return p == x
        """

        # 只需要比较一半就行了，等于对折之后看相等或者不相等
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertNum = 0
        while x > revertNum:       # 判断 x 是不是小于 revertNum ，当它小于的时候，说明数字已经对半或者过半了
            revertNum = revertNum * 10 + x % 10
            x //= 10

        return x == revertNum or x == revertNum // 10  # 奇数的话revertNum要去掉尾数（即原来的中间的数），偶数直接比较


test = Solution()
a = test.isPalindrome(121)
print(a)

