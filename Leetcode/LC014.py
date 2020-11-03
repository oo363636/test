"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:

    def longestCommonPrefix(self, strs: [str]) -> str:

        # 这里是纵向比较，每个词的第一个比较，都相同则下一个字母，否则返回
        if not strs:
            return ''

        length = len(strs[0])
        count = len(strs)

        for i in range(length):
            c = strs[0][i]

            for j in range(count):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]

        return strs[0]


""" 这里是横向比较，一个词跟下一个词比较，返回最长匹配，然后再跟下一个词比较
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
"""


test = Solution()
a = test.longestCommonPrefix(['abc', 'abccc', 'abc'])
print(a)