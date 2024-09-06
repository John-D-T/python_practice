# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root):
        def explore(root):
            root_str = root.val

            if root.left:
                left_exp = "(" + explore(root=root.left) + ")"
            else:
                left_exp = ""

            if root.right:
                right_exp = "(" + explore(root=root.right) + ")"
                if not root.left:
                    left_exp = "()"
            else:
                right_exp = ""

            return f"{root_str}{left_exp}{right_exp}"

        if root is None:
            return None

        return explore(root)

