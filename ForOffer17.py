"""输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999"""


class ForOffer17:

    # def print_numbers(self, n: int) -> [int]:
    #     res = []
    #     for i in range(1, 10 ** n):
    #         res.append(i)
    #     return res

    def print_numbers(self, n: int):
        def dfs(x):
            if x == n:
                s = ','.join(num[self.start:])
                if s != '0':
                    res.append(s)
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num = ['0'] * n
        res = []
        self.nine = 0
        self.start = n-1
        dfs(0)
        return res


if __name__ == '__main__':
    test = ForOffer17()
    print(test.print_numbers(2))