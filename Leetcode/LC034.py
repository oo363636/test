"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]
"""


class Solution:

    def searchRange(self, nums: [int], target: int) -> [int]:
        left_idx = self.insertIndex(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.insertIndex(nums, target, False) - 1]

    def insertIndex(self, nums, target, is_left):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (is_left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1

        return low


test = Solution()
a = test.searchRange([5, 7, 7, 8, 8, 10], 7)  # [1, 2]
print(a)
