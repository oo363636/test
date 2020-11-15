"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
"""


class Solution:

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = Solution.ListNode(0)
        dummy.next = head
        temp = dummy

        # 虚拟一个头节点出来，然后tmp->node1->node2变成tmp->node2->node1，迭代
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = temp.next.next
        return dummy.next


"""递归方法
if not head or not head.next:
    return head
newHead = head.next
head.next = self.swapPairs(newHead.next)
newHead.next = head
return newHead
"""