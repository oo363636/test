"""输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分"""


class ForOffer21:

    def exchange(self, nums: [int]) -> [int]:
        # odd = []
        # even = []
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 1:
        #         odd.append(nums[i])
        #     else:
        #         even.append(nums[i])
        # while even:
        #     odd.append(even.pop())
        # return odd

        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    test = ForOffer21()
    print(test.exchange([1, 2, 3, 4]))

