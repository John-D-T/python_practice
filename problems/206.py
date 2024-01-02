# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # start from the beginning

        # as we're iterating through the linked list, we're gradually changing the pointers so that they point backwards

        # can use a previous and a current to do this

        previous, current = None, head

        # until current is None, we want to iterate. By the time current is None, we're done.

        while current:
            # have the current.next be None (which is what previous is)

            # then have the previous become current (for the next iteration)

            # then current becomes current.next (for the next iteration)

            current.next, previous, current = previous, current, current.next

        # over time, previous becomes the reversed linked list

        return previous



