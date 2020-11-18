"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合
"""


class Solution:

    def generateParenthesis(self, n: int) -> [str]:

        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))

            if left < n:  # 左括号的数量小于N
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()

            if right < left:  # 右括号的数量小于左括号的数量
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


test = Solution()
a = test.generateParenthesis(2)
print(a)  # ['(())', '()()']

