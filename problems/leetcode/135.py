class Solution:
    def candy(self, ratings):
        min_candy = [1] * len(ratings)

        sign_list_l_r = []

        for i, rating in enumerate(ratings):
            if i == 0:
                sign_list_l_r.append('+')
            elif ratings[i] < ratings[i - 1]:
                sign_list_l_r.append('-')
            elif ratings[i] == ratings[i - 1]:
                sign_list_l_r.append('=')
            elif ratings[i] > ratings[i - 1]:
                sign_list_l_r.append('+')

        print(sign_list_l_r)

        for i in range(len(min_candy) - 1):
            if i == 0:
                pass
            elif sign_list_l_r[i + 1] == '-':
                pass
            elif sign_list_l_r[i + 1] == '+':
                min_candy[i + 1] = min_candy[i] + 1
            elif sign_list_l_r[i + 1] == '=':
                pass

        for i in range(len(min_candy) - 1, -1, -1):
            if i == len(ratings) - 1:
                pass
            elif (ratings[i] < ratings[i - 1]) and (min_candy[i] >= min_candy[i - 1]):
                min_candy[i] = min_candy[i - 1] + 1
            elif ratings[i] == ratings[i - 1]:
                pass
            elif ratings[i] < ratings[i - 1]:
                pass

        print(min_candy)
        return sum(min_candy)

