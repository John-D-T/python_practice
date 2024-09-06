# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # have two points traversing the linked list
        # one is travelling 2 at a time
        # one is travelling 1 at a time
        # if the second one catches up then it's a cycle?

        first_pointer = head
        second_pointer = head.next

        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next

            print(first_pointer)
            print(second_pointer)

            if second_pointer == first_pointer:
                return True

        return False

