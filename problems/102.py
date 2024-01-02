# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # create an empty list - traversal_list
        # start at the root
        #     add the list of the root to traversal_list
        # then move down one level
        # repeat

        # how do I explore different branches at the same level at the same time?
        # append them to a list, to be all iterated through at the same time

        traversal_list = []

        def explore_level(node_list):
            temp_list = []
            level_list = []

            for node in node_list:
                if node:
                    level_list.append(node.val)
                    temp_list.append(node.left)
                    temp_list.append(node.right)

            node_list = temp_list

            if level_list:
                traversal_list.append(level_list)

            if node_list:
                explore_level(node_list=node_list)

        explore_level([root])

        return traversal_list


