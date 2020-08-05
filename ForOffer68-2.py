"""给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。"""


class ForOffer6800:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (not root) or (root == p) or (root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == '__main__':
    """                    3
                         /  \
                        5    1
                       / \  / \
                      6  2  0  8
                        / \
                       7  4
    """
    root1 = ForOffer6800.TreeNode(3)
    root1.left = ForOffer6800.TreeNode(5)
    root1.right = ForOffer6800.TreeNode(1)
    root1.left.left = ForOffer6800.TreeNode(6)
    root1.left.right = ForOffer6800.TreeNode(2)
    root1.left.right.left = ForOffer6800.TreeNode(7)
    root1.left.right.right = ForOffer6800.TreeNode(4)
    root1.right.left = ForOffer6800.TreeNode(0)
    root1.right.right = ForOffer6800.TreeNode(8)
    root2 = ForOffer6800()
    res = root2.lowestCommonAncestor(root=root1, p=ForOffer6800.TreeNode(5)
                                     , q=ForOffer6800.TreeNode(4))
    print(res)

"""Traceback (most recent call last):
  File "D:/PyCharmProject/test/ForOffer68-2.py", line 44, in <module>
    print(res.val)
AttributeError: 'NoneType' object has no attribute 'val'
"""
