"""定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点"""


class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def reverse_list(self, head: ListNode) -> ListNode:
        # stack = []     # Stack
        # cur = head
        # while cur:
        #     stack.append(cur.val)
        #     cur = cur.next
        # cur = head
        # while head:
        #     head.val = stack.pop()
        #     head = head.next
        # return cur

        """双指针迭代，我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
第二个指针 cur 指向 head，然后不断遍历 cur。
每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。"""

        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    test = Solution()
    node1 = Solution.ListNode(1)
    node2 = Solution.ListNode(2)
    node3 = Solution.ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    print(test.reverse_list(node1))
