class Solution:
    def candy(self, ratings):
        min_candy = [1] * len(ratings)

        l_to_r_list = []

        r_to_l_list = []
        # generate l to r list
        for i in range(len(ratings)):
            if i == 0:
                l_to_r_list.append('=')
            elif ratings[i] > ratings[i - 1]:
                l_to_r_list.append('+')
            elif ratings[i] <= ratings[i - 1]:
                l_to_r_list.append('=')

        # generate r to l list
        for i in range(len(ratings)):
            if i == len(ratings) - 1:
                r_to_l_list.append('=')
            elif ratings[i] > ratings[i + 1]:
                r_to_l_list.append('+')
            elif ratings[i] == ratings[i + 1]:
                r_to_l_list.append('=')
            elif ratings[i] < ratings[i + 1]:
                r_to_l_list.append('-')

        # work from l to r
        for i in range(len(ratings)):
            if i == 0:
                pass
            elif l_to_r_list[i] == '+':
                min_candy[i] = min_candy[i - 1] + 1

        # work from r to l
        for i in range(len(ratings) - 1, -1, -1):
            if i == len(ratings) - 1:
                pass
            elif r_to_l_list[i] == '+':
                min_candy[i] = min_candy[i + 1] + 1
                # this is to catch situations where the candy increases, but not by enough
                if i != 0:
                    if (r_to_l_list[i - 1] == '-') and (min_candy[i - 1] >= min_candy[i]):
                        min_candy[i] = min_candy[i - 1] + 1
        print(min_candy)
        return sum(min_candy)