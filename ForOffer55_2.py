"""输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，
那么它就是一棵平衡二叉树"""


class Solution:

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def is_balanced(self, root: TreeNode) -> bool:

        """
        后序遍历+剪枝
        左右子树差小于等于1，返回左右子树深度最大值+1；左右子树深度差大于1，返回-1，表示非平衡
        所以碰到-1直接返回-1，提前结束
        """
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            if abs(left - right) <= 1:  # 可用三元运算符
                return max(left, right) + 1
            else:
                return -1

        if recur(root) == -1:   # return recur(root) != -1
            return False
        else:
            return True


if __name__ == '__main__':
    root = Solution.TreeNode(3)
    root.left = Solution.TreeNode(9)
    root.right = Solution.TreeNode(20)
    root.right.left = Solution.TreeNode(15)
    root.right.right = Solution.TreeNode(7)

    test = Solution()
    a = test.is_balanced(root)
    print(a)  # True
