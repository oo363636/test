"""输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）"""


class ForOffer06:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def reverse_print(self, head: ListNode) -> [int]:
        """辅助栈，FILO"""
        res = []
        if not head:
            return []
        while head:
            res.append(head.val)
            head = head.next
        return list(reversed(res))


if __name__ == '__main__':
    test = ForOffer06()
    node1 = ForOffer06.ListNode(4)
    node2 = ForOffer06.ListNode(6)
    node3 = ForOffer06.ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    print(test.reverse_print(node1))

"""
    递归法
    return self.reversePrint(head.next) + [head.val] if head else []
"""