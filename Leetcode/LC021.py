class Solution:

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 递归解法
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1
        #
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        #迭代解法
        dummy = Solution.ListNode(0)
        cur = dummy

        while l1 and l2:

            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if not l2 else l2

        return dummy.next

