"""请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的"""


class Solution:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def is_symmetric(self, root: TreeNode) -> bool:

        def dfs(L, R):
            if not L and not R:     # 当 L 和 R 同时越过叶节点： 此树从顶至底的节点都对称，因此返回 true
                return True
            if not L or not R or L.val != R.val:  # 当L或R中只有一个越过叶节点,不对称；当节点L值不等于R值，不对称
                return False
            return dfs(L.right, R.left) and dfs(L.left, R.right)  # 两对节点对称才是True，所以用and

        if not root:
            return True
        else:
            return dfs(root.left, root.right)


if __name__ == '__main__':
    root = Solution.TreeNode(4)
    root.left = Solution.TreeNode(2)
    root.right = Solution.TreeNode(2)
    root.left.left = Solution.TreeNode(3)
    root.left.right = Solution.TreeNode(4)
    root.right.left = Solution.TreeNode(4)
    root.right.right = Solution.TreeNode(3)
    test = Solution()
    print(test.is_symmetric(root))