"""字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"
"""


class Solution:

    def reverse_left_words(self, s: str, n: int) -> str:
        res = [s[n: len(s)], s[:n]]
        return ''.join(res)


if __name__ == '__main__':
    test = Solution()
    print(test.reverse_left_words('abcdef', 2))


"""
    1)字符串切片
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
        
    2）列表遍历拼接
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])   # 取余，简化代码
        return ''.join(res)   

    3）字符串遍历拼接
    def reverseLeftWords(self, s: str, n: int) -> str:  # 每轮新建字符串，效率低下
        res = ""
        for i in range(n, n + len(s)):
            res += s[i % len(s)]
        return res

"""