"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素
"""


class Solution:

    def removeElement(self, nums: [int], val: int) -> int:

        # 双指针，直接从0开始将不等于val的覆盖到前面去
        # ans = 0
        # for num in nums:
        #     if num != val:
        #         nums[ans] = num
        #         ans += 1
        # return ans

        # 双指针，当前元素跟最后一个元素交换，然后最后一个元素释放
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] == val:
                nums[i] = nums[size - 1]
                size -= 1
            else:
                i += 1

        return size


test = Solution()
a = test.removeElement([4, 5], 4)
print(a)