"""请实现一个函数，把字符串 s 中的每个空格替换成"%20"。"""


class ForOffer05:
    def replace_space(self, s) -> str:
        """实现一个函数，新建res列表，遍历字符串，遇到空格则添加%20到res，否则添加字符串s的内容
        注意了解列表转成字符串方法：''.join(res)，使用join函数"""

        res = []
        for i in s:
            if i != ' ':
                res.append(i)
            if i == ' ':
                res.append('%20')
        return ''.join(res)


if __name__ == '__main__':
    test = ForOffer05()
    print(test.replace_space('  abcd ddd dd'))  # %20%20abcd%20ddd%20dd
