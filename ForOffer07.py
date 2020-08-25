"""输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字"""


class ForOffer07:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    #
    # def build_tree(self, preorder, inorder) -> TreeNode:
    #