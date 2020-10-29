"""给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头
"""


class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = Solution.ListNode(0)
        cur = head
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            _sum = n1 + n2 + carry
            carry = _sum // 10

            cur.next = Solution.ListNode(_sum % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            cur.next = Solution.ListNode(carry)

        return head.next




test = Solution()
node3 = test.ListNode(9)
node2 = test.ListNode(9, node3)
node1 = test.ListNode(9, node2)

l_node2 = test.ListNode(9)
l_node1 = test.ListNode(9, l_node2)

a = test.addTwoNumbers(l_node1, node1)
print(a)