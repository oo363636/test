"""从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，
A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14
"""


class Solution:

    def is_straight(self, nums: [int]) -> bool:
        """1、若无重复的牌（大小王除外）
           2、最大牌 - 最小牌 < 5（大小王除外）
           则5张牌可以构成顺子

        两种方法：集合+遍历   or   排序+遍历，目的都是一致的
        """
        repeat = set()
        max_num = 0
        min_num = 14
        for num in nums:
            if num == 0:
                continue
            if num in repeat:
                return False
            repeat.add(num)
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        return max_num - min_num < 5


if __name__ == '__main__':
    test = Solution()
    a = test.is_straight([0, 0, 2, 5, 3])  # True
    print(a)


""" 排序 + 遍历
def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

作者：jyd
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""