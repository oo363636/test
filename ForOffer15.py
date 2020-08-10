"""请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。
因此，如果输入 9，则该函数输出 2"""

class ForOffer15:

    def hamming_weight(self, n: int) -> int:
        count = 0
        while n != 0:
            weight = n % 2
            if weight == 1:
                count += 1
            n = n // 2
        return count


if __name__ == '__main__':
    test = ForOffer15()
    print(test.hamming_weight(9))


"""
(n−1) 解析： 二进制数字 n 最右边的 1 变成 0 ，此 1 右边的 0 都变成 1 。
n &(n−1) 解析： 二进制数字 n 最右边的 1 变成 0 ，其余不变。
def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

作者：jyd
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""