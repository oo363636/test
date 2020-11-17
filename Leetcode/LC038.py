"""
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串
"""


class Solution:

    def countAndSay(self, n: int) -> str:

        pre = ''
        cur = '1'

        # 第二项开始
        for _ in range(1, n):

            pre = cur  # 这里注意要将 cur 赋值给 pre
            cur = ''  # 因为当前项，就是下一项的前一项。有点绕，尝试理解下
            start = end = 0

            while end < len(pre):

                # 统计重复元素的次数，出现不同元素时，停止
                # 记录出现的次数，
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1

                # 元素出现次数与元素进行拼接
                cur += str(end - start) + pre[start]
                # 初始化start
                start = end

        return cur


test = Solution()
a = test.countAndSay(4)
print(a)