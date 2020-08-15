"""请完成一个函数，输入一个二叉树，该函数输出它的镜像"""


class Solution:

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def mirror_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.mirror_tree(root.right), self.mirror_tree(root.left)
        # 如果不平行赋值，就要用tmp先存储left或者right，否则递归赋值的时候该节点已经被改变了
        return root


if __name__ == '__main__':
    root = Solution.TreeNode(4)
    root.left = Solution.TreeNode(2)
    root.right = Solution.TreeNode(7)
    root.left.left = Solution.TreeNode(1)
    root.left.right = Solution.TreeNode(3)
    root.right.left = Solution.TreeNode(6)
    root.right.right = Solution.TreeNode(9)
    test = Solution()
    test.mirror_tree(root)