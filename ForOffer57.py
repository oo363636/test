"""输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。
"""


class Solution:

    def two_sum(self, nums: [int], target: int) -> [int]:
        """双指针法"""
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:  # nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    test = Solution()
    a = test.two_sum([2, 7, 11, 15], 9)
    print(a)