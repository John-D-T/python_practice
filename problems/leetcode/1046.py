"""
Key operations

    heapq.heapify
    heapq.heappush
    heapq.heappop
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # we're focused on the two heaviest elements in an array, so opting for a maxheap makes sense

        # to do so, I'll convert the list of stones to negative, then apply a minheap

        maxHeap = [(-1 * stone) for stone in stones]

        heapq.heapify(maxHeap)

        # next is comparing the top two stones
        # but first I want to create a loop so the upcoming steps end once we have a small enough heap
        while len(maxHeap) > 1:

            first_stone = heapq.heappop(maxHeap)
            second_stone = heapq.heappop(maxHeap)

            # remember that we're dealing with negatives here
            if first_stone < second_stone:
                remaining_stone = first_stone - second_stone
                heapq.heappush(maxHeap, remaining_stone)

            # can assume the else would be their equal
            else:
                pass

        if len(maxHeap) > 0:
            return -1 * heapq.heappop(maxHeap)

        # if len(maxHeap) == 0
        else:
            return 0

