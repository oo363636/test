"""在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class ForOffer04:
    def find_number_in_2Darray(self, matrix, target) -> bool:
        """线性查找，从左下角开始，target大于该值则往右查找，target小于该值则往上查找
        时间复杂度为O（m+n）
        同理可以从右上角开始查找"""

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        columns = len(matrix[0])
        row = rows-1
        column = 0
        while row >= 0 and column < columns:
            number = matrix[row][column]
            if target == number:
                return True
            elif target >= number:
                column += 1
            else:
                row -= 1
        return False


if __name__ == '__main__':
    find = ForOffer04()
    res = find.find_number_in_2Darray([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 21)

    print(res)
