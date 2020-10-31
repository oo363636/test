"""给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串
"""


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        """如果符合条件，一定是偶数长度，可以加这个判断"""
        if len(s) % 2 == 1:
            return False

        stack = []
        dic = {         # 存储hashtable，快速判断是否形成闭合的括号
               ')': '(',
               ']': '[',
               '}': '{'
        }

        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack


test = Solution()
a = test.isValid('')
print(a)