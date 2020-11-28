"""
给定一个二叉树，检查它是否是镜像对称的
"""


class Solution:
    """
    如果同时满足下面的条件，两个树互为镜像：
    它们的两个根结点具有相同的值
    每个树的右子树都与另一个树的左子树镜像对称
    """
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)

    def check(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)