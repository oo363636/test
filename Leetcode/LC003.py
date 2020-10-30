"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """ 我写的复杂度太高，运行时间长，可以优化
        if not s:
            return 0

        longest_count = 1
        for i in range(len(s)):
            count = 1
            is_repeat = set(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in is_repeat:
                    is_repeat.add(s[j])
                    count += 1
                else:
                    break
                if count > longest_count:
                    longest_count = count

        return longest_count
        """

        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:    # while可以，不能用if，因为连续重复的要删掉重复的为为止
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


test = Solution()
a = test.lengthOfLongestSubstring('pwwkew')
print(a)  # 3
