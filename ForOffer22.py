"""输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点
"""


class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def get_kth_end(self, head: ListNode, k: int) -> ListNode:
        # cur = head                 # 遍历一遍得到链表长度n，然后倒数第k个找出来
        # count = 0
        # while cur:
        #     count += 1
        #     cur = cur.next
        # count2 = 0
        # cur2 = head
        # while cur2 and count2 != count - k:
        #     cur2 = cur2.next
        #     count2 += 1
        # return cur2

        pre = lat = head        # 双指针，使前后指针相隔k，这样当后指针为空的时候，前指针恰好为倒数第k个
        while k != 0:
            lat = lat.next
            k -= 1
        while lat:
            lat = lat.next
            pre = pre.next
        return pre


if __name__ == '__main__':
    test = Solution()
    node1 = Solution.ListNode(1)
    node2 = Solution.ListNode(2)
    node3 = Solution.ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    print(test.get_kth_end(node1, 2).val)