class Solution:
    def productExceptSelf(self, nums):
        # start with an output_list, with all values as 1 - this is our base point

        output_list = [1] * len(nums)

        # goal:

        # pre_list = [1,2,6,24]
        # post_list = [24,24,12,4]

        # output_list = [1*24, 1*12, 2*4, 6*1]

        # start with a value of 1
        value = 1
        for i in range(1, len(nums), 1):
            value = value * nums[i - 1]
            output_list[i] = output_list[i] * value

        value = 1
        for i in range(len(nums) - 2, -1, -1):
            # range with a stop of -1 means the 0 is included
            value = value * nums[i + 1]
            output_list[i] = output_list[i] * value

        return output_list


