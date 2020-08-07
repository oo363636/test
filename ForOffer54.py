"""给定一棵二叉搜索树，请找出其中第k大的节点。"""


class ForOffer54:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def kth_largest(self, root, k):
        """中序遍历的逆顺序，每次遍历k-1，当k=0即找到res，保存res，并退出遍历"""
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


if __name__ == '__main__':
    """                 6
                       /  \
                      2    8
                     / \  / \
                    0  4  7  9
                      / \
                     3  5
    """
    root1 = ForOffer54.TreeNode(6)
    root1.left = ForOffer54.TreeNode(2)
    root1.right = ForOffer54.TreeNode(8)
    root1.left.left = ForOffer54.TreeNode(0)
    root1.left.right = ForOffer54.TreeNode(4)
    root1.left.right.left = ForOffer54.TreeNode(3)
    root1.left.right.right = ForOffer54.TreeNode(5)
    root1.right.left = ForOffer54.TreeNode(7)
    root1.right.right = ForOffer54.TreeNode(9)
    a = ForOffer54()
    print(a.kth_largest(root1, 3)) # 7

