"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

跟interview1001一样
"""


class Solution:

    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:

        i = m - 1
        j = n - 1

        for k in range(m + n - 1, -1, -1):

            if i == -1 and j != -1:
                nums1[k] = nums2[j]
                j -= 1

            elif i != -1 and j == -1:
                nums1[k] = nums1[i]
                i -= 1

            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


test = Solution()
a = test.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)