"""找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
"""


class ForOffer03:
    def find_repeat_number(self, nums: [int]) -> int:
        """利用集合set"""

        dd = set()
        for num in nums:
            if num in dd:
                return num
            dd.add(num)
        return -1


if __name__ == '__main__':
    frn = ForOffer03()
    print(frn.find_repeat_number([1, 2, 3, 3, 3, 4, 4, 5, 4, 6]))


"""
原地交换，利用“在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内”的信息，使值和索引一一对应
第一次遇到数字x，交换至索引x处，第二次遇见x时，则为重复数字
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
"""