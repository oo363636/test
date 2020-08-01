"""输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。"""

class ForOffer42:
    def maxSubArray(self,nums):

        for i in range(1,len(nums)):
            nums[i] += max(nums[i-1],0)

        return max(nums)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(ForOffer42.maxSubArray(ForOffer42,nums))