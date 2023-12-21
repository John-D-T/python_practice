class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # since it's sorted, we don't have to sort - we can just start from the middle

        # we have a left pointer and right pointer - these narrow as we perform the binary search

        # Nest the next steps in a while loop - we're doing this until we get the value we want
        # The loop only ends if the left pointer is strictly less than the right?

        # we find the midpoint

        # is the target less than the midpoint? If so, move the right pointer to the middle point

        # is the target more than the midpoint, If so, move the left pointer to the middle point

        # is it equal to the midpoint? If so, return the value

        # If we reach here, it means the target wasn't to be found. Return -1
