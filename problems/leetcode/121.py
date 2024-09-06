def find_max_profit(prices):
    """
    :param prices: List[int]
    :return: int
    """
    # can we look to be greedy
    # create a left pointer, and right pointer
    l, r = 0, 1

    # also create a variable called 'max_profit', set it to 0
    max_profit = 0

    # right pointer must also be in the list's range (use len())
    # left must always be less than the right pointer, but that's not an issue here
    while r < len(prices):

        # calculate the difference between the right and left pointer (right-left)
        difference = prices[r] - prices[l]

        # regardless: calculate max(max_profit, difference)
        max_profit = max(max_profit, difference)
        if difference < 0:

            # if it's negative, move the right pointer to where the left_pointer is. The left pointer value is way too high
            l = r
            r += 1

        else:
            # if it's positive or neutral, just move the right pointer right

            r += 1

        return max_profit