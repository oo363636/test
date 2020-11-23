"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列
"""


class Solution:

    def permute(self, nums: [int]) -> [[int]]:

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


test = Solution()
a = test.permute([1, 2, 3])
print(a)
