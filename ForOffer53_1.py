"""统计一个数字在排序数组中出现的次数"""


class Solution:

    def search(self, nums: [int], target: int) -> int:
        # dic = {}
        # for num in nums:
        #     if not num in dic:
        #         dic[num] = 1
        #     else:
        #         dic[num] += 1
        # for k, v in dic.items():
        #     if k == target:
        #         return v
        # return 0
        # 没用上排序这个条件，不要用字典。用二分法

        i, j = 0, len(nums) - 1
        while i <= j:  # 搜索右边界right
            mid = (i + j) // 2
            if nums[mid] <= target:  # 有等于
                i = mid + 1
            else:  # mid > target:
                j = mid - 1
        right = i
        if j >= 0 and nums[j] != target:  # 若数组中无target，则提前返回
            return 0
        i = 0
        while i <= j:  # 搜索左边界left
            mid = (i + j) // 2
            if nums[mid] < target:  # 无等于
                i = mid + 1
            else:  # mid > target:
                j = mid - 1
        left = j
        return right - left - 1


if __name__ == '__main__':
    test = Solution()
    a = test.search([5, 7, 7, 8, 8, 10], 8)
    print(a)  # 2

    #封装起来helper，只查找右边界
"""def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)

作者：jyd
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
