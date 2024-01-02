# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # go through them recursively together
        # until all of them have been covered AND the values match

        def check_nodes(node_1, node_2):
            # we want them to be structurally the same, AND to contain the same values

            # catch for empty nodes
            if not node_1 and not node_2:
                return True

            # catch for if one of the nodes is null
            if (not node_1 and node_2) or (node_1 and not node_2):
                return False

            # we then check that:
            # 1. the left nodes match
            # 2. the right nodes match
            # 3. the values match
            left_check = check_nodes(node_1.left, node_2.left)
            right_check = check_nodes(node_1.right, node_2.right)
            val_check = node_1.val == node_2.val

            equal = val_check and left_check and right_check

            return equal

        check = check_nodes(p, q)

        return check
