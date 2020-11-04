"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n
"""


class Solution:

    def merge(self, A: [int], m: int, B: [int], n: int) -> None:

        # 将最大的放在最后，从后往前
        tail = m + n - 1
        pa = m - 1
        pb = n - 1

        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                # A[tail] = A[pa]   # 感觉这行有点多余，注释掉
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:  # A[pa] <= B[pb]:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1


test = Solution()
test.merge([1, 2, 5, 0, 0], 3, [2, 4], 2)
