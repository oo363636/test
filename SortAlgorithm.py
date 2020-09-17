# insertion sort插入排序
class InsertionSort:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            cur = arr[i]
            pre_index = i - 1
            while pre_index >= 0 and arr[pre_index] > cur:
                arr[pre_index + 1] = arr[pre_index]
                pre_index -= 1
            arr[pre_index + 1] = cur
        return arr


# shell sort希尔排序（跟插入排序有联系）
class ShellSort:
    def shell_sort(self, arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):  # 从数组第gap个元素开始
                if arr[i] < arr[i - gap]:
                    cur = arr[i]
                    pre_index = i - gap
                    while pre_index >= 0 and arr[pre_index] > cur:
                        arr[pre_index + gap] = arr[pre_index]
                        pre_index -= gap
                    arr[pre_index + gap] = cur
            gap //= 2
        return arr


# merge sort归并排序（分治）
class MergeSort:

    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res


if __name__ == '__main__':
    arr = [1, 4, 7, 2, 3, 1]
    # insertion_sort_arr = InsertionSort().insertion_sort(arr)
    # shell_sort_arr = ShellSort().shell_sort(arr)
    # print(insertion_sort_arr)
    # print(shell_sort_arr)
    merge_sort_arr = MergeSort().sort(arr)
    print(merge_sort_arr)
