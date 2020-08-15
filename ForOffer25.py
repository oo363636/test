"""输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的"""


class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dum = cur = Solution.ListNode(0)        # 暴力解法，新建虚拟头节点，在节点之后不断添加元素较小的节点
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        # while not l1 and l2:
        #     cur.next = l2
        #     l2 = l2.next
        #     cur = cur.next
        # while l1 and not l2:
        #     cur.next = l1
        #     l1 = l1.next
        #     cur = cur.next
        cur.next = l1 if l1 else l2   # 上面这一串逻辑可以用三元表达式简化
        return dum.next


if __name__ == '__main__':
    l1_node1 = Solution.ListNode(1)
    l1_node2 = Solution.ListNode(2)
    # l1_node3 = Solution.ListNode(4)
    l2_node1 = Solution.ListNode(1)
    l2_node2 = Solution.ListNode(3)
    l2_node3 = Solution.ListNode(4)

    l1_node1.next = l1_node2
    # l1_node2.next = l1_node3
    # l1_node3.next = None
    l1_node2.next = None
    l2_node1.next = l2_node2
    l2_node2.next = l2_node3
    l2_node3.next = None

    test = Solution()
    test.merge_two_lists(l1_node1, l2_node1)


"""
    递归方法：
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""