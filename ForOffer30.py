"""定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)"""


class Solution:
    """使用双栈维护最小值，使得min复杂度为O（1）
    B存储A中的非严格降序的元素，所以等于也放入B"""
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A[-1] == self.B[-1]:
            self.B.pop()
        self.A.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]


if __name__ == '__main__':
    test = Solution()
    test.push(-2)
    test.push(0)
    test.push(-3)
    print(test.min())  # -3
    test.pop()
    print(test.top())  # 0
    print(test.min())  # 2