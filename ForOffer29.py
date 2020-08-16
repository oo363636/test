"""输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字"""


class Solution:

    def spiral_order(self, matrix: [[int]]) -> [int]:
        """定义四个边界l、r、t、b，不断输出数组内容并缩小边界，直到超出边界"""
        res = []
        if not matrix:
            return res
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b: break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res


if __name__ == '__main__':
    test = Solution()
    mm = test.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    nn = test.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(mm)  # [1,2,3,6,9,8,7,4,5]
    print(nn)  # [1,2,3,4,8,12,11,10,9,5,6,7]
