# WIP

class Solution:
    def convert(self, s: str, numRows):
        pass
# so we want to figure out
# how to convert it to a zigzag string
# read that new string pattern line by line

# one potentially helpful tip: every numRows'th column, it will be fully filled
# this means every:
# numRows + 1 character will be on the numRows - 1 rows
# numRows + 2 character will be on the numRows - 2 rows
# and so on

# this means the first row will be the 1st, (numRows + (numRows-2) + 1)th, (2numRows + 2(numRows-2) + 1)th
# second row will be the 2nd, numRows + 2, 2numRows + 2(2)

# can i create a bunch of categorizations in a hashmap:
    # e.g. {row_1: [PIN]}
    #      {row_2: [ALSING]}