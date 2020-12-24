"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历
"""


class Solution:

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def inorderTraversal(self, root: TreeNode) -> [int]:

        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

        res = []
        dfs(root, res)
        return res