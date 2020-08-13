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


"""def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# 递归终止条件是当前为空，或者下一个节点为空
		if(head==None or head.next==None):
			return head
		# 这里的cur就是最后一个节点
		cur = self.reverseList(head.next)
		# 这里请配合动画演示理解
		# 如果链表是 1->2->3->4->5，那么此时的cur就是5
		# 而head是4，head的下一个是5，下下一个是空
		# 所以head.next.next 就是5->4
		head.next.next = head
		# 防止链表循环，需要将head.next设置为空
		head.next = None
		# 每层递归函数都返回cur，也就是最后一个节点
		return cur

作者：wang_ni_ma
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/dong-hua-yan-shi-duo-chong-jie-fa-206-fan-zhuan-li/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""