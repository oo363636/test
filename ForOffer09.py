"""用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )"""


class ForOffer09:
    """stack1来添加，stack2来删除
    当stack2空时，看看stack1有什么元素，给append进stack2
    如果stack1没元素，则stack2还是空，return -1
    如果stack1有元素，则正常pop stack2的元素，即为head元素"""

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        else:
            return self.stack2.pop()


if __name__ == '__main__':
    ss = ForOffer09()
    print(ss.appendTail(2))
    print(ss.appendTail(4))
    print(ss.deleteHead())