"""给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点"""


class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = Solution.ListNode(0, head)  # 要起一个dummy比较好操作
        cur = head
        mark = dummy

        while n > 0:
            cur = cur.next
            n -= 1

        while cur:
            dummy = dummy.next
            cur = cur.next

        dummy.next = dummy.next.next
        return mark.next  # 要返回虚拟节点dummy的下一个节点，因为head有可能被删除了，就会出问题


test = Solution()
node1 = Solution.ListNode(5)
node2 = Solution.ListNode(4, node1)
node3 = Solution.ListNode(3, node2)
node4 = Solution.ListNode(2, node3)
node5 = Solution.ListNode(1, node4)

test.removeNthFromEnd(node5, 2)
