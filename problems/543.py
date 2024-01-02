# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # for each node, look at the two deepest paths for each subtree
        #   add those two number up, then that's the local_max
        #   then explore the subtrees and do the same
        #   compare all these local maxes in a heap or stack?

        stack = []
        queue = [root]

        while queue:
            # pop the node from the queue
            node = queue.popleft()

            # explore the deepest parts of both subtrees of the node
            local_left_stack = [[node, 0]]
            local_left_max = 0

            local_right_stack = [[node, 0]]
            local_right_max = 0

            # retrieve the max depth for both subtrees
            if node.left:
                while local_left_stack:
                    node, depth = local_left_max.popleft()

                    # have an if node check
                    # if it's populated, then we consider it's depth in the local_left_max variable

                    # append left and right to the local_left_stack

            if node.right:
                while local_right_stack:
                    node, depth = local_right_max.popleft()

            # add these up to form the local_max
            local_max = local_left_max + local_right_max

            # append [local_max] to the stack
            if stack:
                current_max = stack.pop()
                stack.append(max(current_max, local_max))
            else:
                stack.append(local_max)

            # append the subtrees to the queue, until we have no more nodes to explore
            # TODO - maybe can perform a node check instead of a node.left check. may need to refactor other code
            if node.left:
                queue.append([node.left])
            if node.right:
                queue.append([node.right])
