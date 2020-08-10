"""给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点"""


class ForOffer18:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def delete_node(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        pre_node = head
        cur_node = head.next

        while cur_node and cur_node.val != val:
            # if val != cur_node.val:
            pre_node = pre_node.next
            cur_node = cur_node.next
        if val == cur_node.val:
            pre_node.next = cur_node.next
            cur_node.next = None
        return head

        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res


if __name__ == '__main__':
    test = ForOffer18()
    node1 = ForOffer18.ListNode(4)
    node2 = ForOffer18.ListNode(5)
    node3 = ForOffer18.ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = None
    t = test.delete_node(node1, 4)
    print(t.val)
    print(t.next.val)
    print(t.next.next.val)


"""
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: 
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: 
            pre.next = cur.next
        return head

作者：jyd
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/mian-shi-ti-18-shan-chu-lian-biao-de-jie-dian-sh-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""