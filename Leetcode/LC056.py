"""
给出一个区间的集合，请合并所有重叠的区间
"""


class Solution:

    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        merge = []

        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merge[-1][1] = max(merge[-1][1], interval[1])

        return merge


test = Solution()
a = test.merge([[1, 3], [2, 6], [8, 10], [15, 18]])  # [[1, 6], [8, 10], [15, 18]]
print(a)
