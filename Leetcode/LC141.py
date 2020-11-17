"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false
"""


class Solution:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def hasCycle(self, head: ListNode) -> bool:

        # 最容易想到的方法是遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过
        # seen = set()
        #
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False

        # 快慢指针,「Floyd 判圈算法」（又称龟兔赛跑算法）有所了解
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:  # 注意这块的判断条件，我自己写写错了
                return False
            slow = slow.next  # slow走一格
            fast = fast.next.next  # fast走两格

        return True


test = Solution()
node1 = Solution.ListNode(3)
node2 = Solution.ListNode(2)
node3 = Solution.ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node2

a = test.hasCycle(node1)