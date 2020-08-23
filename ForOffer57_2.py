"""输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列"""


class Solution:

    def find_continuous_sequence(self, target: int) -> [[int]]:
        i = j = 1  # 左闭区间、右开区间
        num_sum = 0  # 滑动窗口中数字的和
        res = []
        while i <= target // 2:
            if num_sum < target:
                # 右边界向右移动
                num_sum += j
                j += 1
            elif num_sum > target:
                # 左边界向右移动
                num_sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i,j))
                res.append(arr)
                # 左边界向右移动
                num_sum -= i
                i += 1
        return res


if __name__ == '__main__':
    test = Solution()
    a = test.find_continuous_sequence(9)
    print(a)  # [[2, 3, 4], [3, 4]]
    b = test.find_continuous_sequence(15)
    print(b)  # [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
