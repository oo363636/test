"""输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I
"""


class Solution:

    def reverse_words(self, s: str) -> str:
        res = []
        s = s.strip()  # 删除首位空格
        i = j = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] != ' ':  # 搜索首个空格
                i -= 1
            res.append(s[i + 1: j + 1])  # 添加单词
            while s[i] == ' ':  # 跳过单词间空格
                i -= 1
            j = i  # j指向下个单词的尾字符
        return ' '.join(res)  # 拼接并返回


if __name__ == '__main__':
    test = Solution()
    ss = test.reverse_words('  I am  a bb ')
    print(ss)  # bb a am I
