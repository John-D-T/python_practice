# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # go first, last, second, second, last, etc

        # create a copy of the linked list which is reversed?

        # then go first from normal, first from reversed, etc...?

        # or I find the midpoint using double pointers, then reverse the second half?

        # finding the midpoint
        one_step = head
        two_step = head.next

        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next

        # reverse the one_step now
        # print(f'one step: {one_step}')
        # print(f'two step: {two_step}')

        current = one_step.next

        # print(f'head {head}')
        one_step.next = None
        # print(f'head {head}')

        previous = None

        while current:
            current.next, previous, current = previous, current, current.next

        # now we have previous and the original head
        first, second = head, previous
        # print(first)
        # print('second: %s' % second)

        # print('-----')

        while second:
            # print('first %s' % first)
            # print('second %s' % second)
            # print('head %s' % head)
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            # move on to the next for both
            first, second = tmp1, tmp2
            # print(head)





