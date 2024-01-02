# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # the left of the node is less - if not return False
        # the right of the node is more - if not return False

        # then run is_valid on the left and right subtrees
        #      this means running the function recursively

        # end point? when left and right are none

        # key thing is establishing global boundaries throughout

        # if we reach the end of the recursion with no issues (no Falses at any point), return True

        def is_valid(node, left_boundary, right_boundary):
            if not node:
                return True

            check_left = node.val > left_boundary
            check_right = node.val < right_boundary

            inner_left_check = is_valid(node=node.left, left_boundary=left_boundary, right_boundary=node.val)
            inner_right_check = is_valid(node=node.right, left_boundary=node.val, right_boundary=right_boundary)

            return check_left and check_right and inner_left_check and inner_right_check

        check = is_valid(root, float('-inf'), float('inf'))

        return check



