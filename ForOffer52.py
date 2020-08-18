"""输入两个链表，找出它们的第一个公共节点"""


class Solution:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，
        然后同时分别逐结点遍历，当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；
        当 node2 到达链表 headB 的末尾时，重新定位到链表 headA 的头结点。
        这样，当它们相遇时，所指向的结点就是第一个公共结点。
        """
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1


if __name__ == '__main__':
    A_node1 = Solution.ListNode(1)
    A_node2 = Solution.ListNode(2)
    A_node3 = Solution.ListNode(3)
    A_node1.next = A_node2
    A_node2.next = A_node3
    A_node3.next = None

    B_node1 = Solution.ListNode(2)
    B_node2 = Solution.ListNode(3)
    B_node1.next = B_node2
    B_node2.next = None

    test = Solution()
    a = test.get_intersection_node(A_node1, B_node1)