"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置
你可以假设数组中无重复元素
"""


class Solution:

    def searchInsert(self, nums: [int], target: int) -> int:

        # 这种查找太慢了，O（n）
        # size = len(nums)
        #
        # if target <= nums[0]:
        #     return 0
        # elif target > nums[size - 1]:
        #     return size
        #
        # for i in range(1, size):
        #     if nums[i] >= target > nums[i - 1]:
        #         return i

        # 二分查找， O（logn）
        size = len(nums)
        left = 0
        right = size - 1
        ans = size  # 这里设置ans为size，就是为了避免这个target比所有数大的时候，没有返回值的状况出现

        while left <= right:

            mid = (left + right) // 2
            if target <= nums[mid]:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


test = Solution()
a = test.searchInsert([1, 3, 5, 6], 7)
print(a)