class Solution:
    def repeatedNTimes(self, nums):
        # one soln: find the key number, loop through list until we count an element which appears that many times

        # 2nd soln: loop through list, and find the first element which appears twice
        unique_list = set()

        for num in nums:
            if num in unique_list:
                return num
            else:
                unique_list.add(num)