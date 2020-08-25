"""请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、
push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1"""
import collections


class MaxQueue:

    def __init__(self):
        self.dequeA = collections.deque()
        self.dequeB = collections.deque()

    def max_value(self) -> int:
        if not self.dequeB:  # 可以用三元运算符
            return -1
        return self.dequeB[0]

    def push_back(self, value: int) -> None:
        self.dequeA.append(value)
        while self.dequeB and self.dequeB[-1] < value:  # 保持dequeB递减
            self.dequeB.pop()
        self.dequeB.append(value)

    def pop_front(self) -> int:
        if not self.dequeA:
            return -1
        if self.dequeA[0] == self.dequeB[0]:
            self.dequeB.popleft()
        return self.dequeA.popleft()


if __name__ == '__main__':
    test = MaxQueue()
    test.push_back(1)
    test.push_back(2)
    print(test.max_value())  # 2
    print(test.pop_front())  # 1
    print(test.max_value())  # 2

