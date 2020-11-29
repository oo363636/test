"""
给你一个整数数组 nums ，和一个整数 target 。

该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找，跟剑指11有点点类似
        if not nums:
            return -1

        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1