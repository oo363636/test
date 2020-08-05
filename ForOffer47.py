"""在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
"""
from typing import List

class ForOffer47:
    def max_value(self, grid:List[List[int]]) -> int:
        # grid[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                if i != 0 and j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                if i != 0 and j != 0:
                    grid[i][j] = grid[i][j] + max(grid[i-1][j],grid[i][j-1])
        return grid[len(grid)-1][len(grid[0])-1]
        # 这里可以用grid[-1][-1]表示最后一行

if __name__ == '__main__':
    mv1 = ForOffer47()
    print(mv1.max_value([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

# 以上对于i==0，j==0的情况，循环每轮都执行，但是[0][0]属于极少数情况，可以进一步优化
"""
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
"""
