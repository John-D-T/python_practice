# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # essentially, every single left and right subtree is switched around

        # so root.left becomes root.right

        # if node is empty, we can just return the root

        def mini_inversion(node):
            if not node:
                pass
            else:
                node.right, node.left = node.left, node.right
                mini_inversion(node=node.left)
                mini_inversion(node=node.right)

        mini_inversion(node=root)

        return root