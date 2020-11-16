"""给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序"""


class Solution:

    def moveZeroes(self, nums: [int]) -> None:

        # 自己写的
        # i = 0
        # j = 0
        # while i < len(nums) and j < len(nums):
        #     if nums[i] != 0:
        #         i += 1
        #     elif nums[j] == 0:
        #         j += 1
        #     elif nums[i] == 0 and nums[j] != 0 and i < j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1

        # 更简洁的写法
        j = 0
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        # 还有一种方法，两次遍历，第一次记录非0的个数，非零全部给nums[j]，然后第二次遍历把后面的置0
        # 这个方法慢了一些些

test = Solution()
a = test.moveZeroes([1, 0])
