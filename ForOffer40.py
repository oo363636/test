"""输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4"""
import heapq


class Solution:
    """Top K 问题，快排 or 堆"""
    def get_least_numbers(self, arr: [int], k: int) -> [int]:
        # arr.sort()
        # res = []
        # for i in range(k):
        #     res.append(arr[i])
        # return res    # return arr[:k] 即可

        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]  # 我们这题需要用大顶堆，而python只有小顶堆，所以取相反数
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if arr[i] < -hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        res = [-x for x in hp]
        return res


if __name__ == '__main__':
    test = Solution()
    a = test.get_least_numbers([3, 2, 1], 2)
    print(a)  # [2,1]