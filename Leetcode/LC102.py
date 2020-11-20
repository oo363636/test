"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）
"""


import collections

class Solution:

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def levelOrder(self, root: TreeNode) -> [[int]]:

        res = []
        queue = collections.deque()

        if root:
            queue.append(root)

        while queue:
            n = len(queue)
            level = []

            for _ in range(n):  # 把同一层的都遍历出来
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res