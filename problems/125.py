"""
Key takeaways:

    Pointers are key
    isalum() is a very helpful in-built python method
    list() is easier than in list comprehension due to simplicity of requirement here.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert it to an iterable to make pointers possible
        # we convert to lower
        s_list = list(s.lower())

        # create the pointers - use len(s_list) -1 to get the last placement in the list
        left_pointer = 0
        right_pointer = len(s_list) - 1

        while left_pointer < right_pointer:
            # if there are non alphanumeric characters, move the pointers past them.
            if not s_list[left_pointer].isalnum():
                left_pointer += 1

            elif not s_list[right_pointer].isalnum():
                right_pointer -= 1

            elif s_list[left_pointer] == s_list[right_pointer]:
                # if the left most and right most match, we bring both sides in by one character. We keep doing so.
                left_pointer += 1
                right_pointer -= 1

            else:
                return False

        # if we have one element left, or none, both will fulfill the palindrome criteria
        return True



