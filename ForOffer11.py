"""把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1"""

class ForOffer11:

    # def min_array(self, numbers: [int]) -> int:
    #     for i in range(1, len(numbers)):
    #         if numbers[i-1] > numbers[i]:
    #             return numbers[i]
    #     return numbers[0]

    def min_array(self, numbers: [int]) -> int:
        """二分查找"""
        min_index, max_index = 0, len(numbers)-1

        while min_index < max_index:
            mid_index = (min_index + max_index) // 2
            if numbers[mid_index] > numbers[max_index]:
                min_index = mid_index + 1
            elif numbers[mid_index] < numbers[max_index]:
                max_index = mid_index        # 这里之前减1，结果出错
            else:
                max_index -= 1
        return numbers[min_index]


if __name__ == '__main__':
    test = ForOffer11()
    print(test.min_array([3, 4, 5, 6, 7, 1, 2]))
    print(test.min_array([0, 1, 2, 3, 4, 5]))
    print(test.min_array([1, 3, 5]))