# this is a DFS or BFS problem

# explore each path, and derive a level from that path

# then calculate the max level from all those levels - thats our maximum depth

# try for a stack

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # create a stack
        # as we dig into the tree, we can add to the stack

        if not root:
            return 0

        stack = [[root, 1]]

        depth = 1

        while stack:
            # pop from the stack, then append the subtrees
            node, level = stack.pop()

            # this 'if' catch is crucial. This means we might have a [None, 8] in the stack, but since it's none, it's not actually a node,
            # so we don't alter the max_depth
            if node:
                depth = max(depth, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])

        return depth

