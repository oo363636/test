"""给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
"""


# 如何表示树，print地址中的内容？

class ForOffer68:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def lowestCommonAncestor(self, root, p, q) -> TreeNode:
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


if __name__ == '__main__':
    root1 = ForOffer68.TreeNode(6)
    root1.left = ForOffer68.TreeNode(2)
    root1.right = ForOffer68.TreeNode(8)
    root1.left.left = ForOffer68.TreeNode(0)
    root1.left.right = ForOffer68.TreeNode(4)
    root1.left.right.left = ForOffer68.TreeNode(3)
    root1.left.right.right = ForOffer68.TreeNode(5)
    root1.right.left = ForOffer68.TreeNode(7)
    root1.right.right = ForOffer68.TreeNode(9)
    root2 = ForOffer68()
    p = root2.lowestCommonAncestor(root=root1, p=ForOffer68.TreeNode(2)
                                   , q=ForOffer68.TreeNode(4))
    print(p)
