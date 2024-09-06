class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        sum_list = []
        sum_even = 0
        # prematurely create a sum of all your even numbers
        for num in nums:
            if num % 2 == 0:
                sum_even += num

        # then loop through queries, and edit as necessary
        for query in queries:
            # unpack the query
            value, index = query[0], query[1]
            previous_value = nums[index]
            current_value = nums[index] + value
            nums[index] = nums[index] + value
            # if the previous value is ODD and current value is EVEN
            # add the current value
            if previous_value % 2 != 0:
                if current_value % 2 == 0:
                    sum_even += current_value
            # if the previous value is ODD and current value is ODD
            # do nothing to sum_even

            if previous_value % 2 == 0:
                if current_value % 2 != 0:
                    sum_even -= previous_value
                if current_value % 2 == 0:
                    sum_even += (current_value - previous_value)
            # if the previous value is EVEN and current value is ODD
            # minus the previous value
            # if the previous value is EVEN and current value is EVEN
            # add curr - prev
            sum_list.append(sum_even)

        return sum_list


