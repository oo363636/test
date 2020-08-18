"""在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母"""


class Solution:

    def first_unique_char(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        # for c in s:
        #     if dic[c]:
        #         return c
        # return ' '
        for k, v in dic.items():   # 有序字典，不用第二次遍历完整个字符串，效率更高
            if v:
                return k
        return ' '


if __name__ == '__main__':
    test = Solution()
    a = test.first_unique_char('abbaddcef')
    print(a)
