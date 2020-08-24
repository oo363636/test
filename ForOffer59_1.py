"""给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值"""
import collections


class Solution:
    # 用双端队列
    def max_sliding_window(self, nums: [int], k: int) -> [int]:
        res = []
        n = len(nums)
        deque = collections.deque()
        for i, j in zip(range(1 - k, n - k + 1), range(0, n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()  # 删除deque中对应的nums[i-1]
            while deque and deque[-1] < nums[j]:
                deque.pop()  # 保持deque递减
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])  # 记录窗口的最大值
        return res


if __name__ == '__main__':
    test = Solution()
    a = test.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(a)  # [3, 3, 5, 5, 6, 7]


"""
形成窗口前和后两个阶段拆分开
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k): # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)): # 形成窗口后
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

作者：jyd
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-i-hua-dong-chuang-kou-de-zui-da-1-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""