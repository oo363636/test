"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组
"""


class Solution:

    def threeSum(self, nums: [int]) -> [[int]]:

        n = len(nums)
        nums.sort()  # 先排序，再用second从first的下一个到最后，third从数组最后到往前，双指针
        res = []

        for first in range(n):

            if first > 0 and nums[first] == nums[first - 1]:  # 要有first>0，否则第一个数都跳过了，【0，0，0】就无输出
                continue

            third = n - 1
            target = -nums[first]

            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:  # 要有second>first+1，第first+1个要留着
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res


test = Solution()
# a = test.threeSum([-1, 0, 1, 2, -1, 4])
a = test.threeSum([0, 0, 0])
print(a)
