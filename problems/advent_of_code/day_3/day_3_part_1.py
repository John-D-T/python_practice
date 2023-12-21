"""
Problem broken down

Missing an engine part

add all 'part numbers' to figure this out

'part_numbers' are numbers adjacent to a symbol (not including '.')
    symbol includes: *, #, +, etc....
    adjacent means next to it on a matrix (diagonals are allowed)

Thus, if a number is completely surrounded by '.' or numbers, it's isolated
    a.k.a Not a part

figure out all numbers which ARE a part
    Then sum these

ideas:

initialize variable 'valid_parts' to be 0

convert into a matrix

then loop through each row

for each row, have a left and right pointer to figure out the width of a number
    once you determine that the number ends (next value isn't a number)
        then perform a check above and below (except if you're the first or last row)
            if any values are not '.' or a number, then you have a part
                if it's a part, append it to 'valid_parts'


then return valid_parts

Soln: what I have: 514745
"""


def sum_part_numbers(matrix):
    valid_parts = 0

    # through each row
    for row_num, line in enumerate(matrix):
        number = ''

        # through each element in a row
        for position in range(len(line)):
            character = line[position]
            if character.isnumeric():
                number += character
            else:
                # skip if it's a period/symbol
                if number != '':
                    start_of_number = position - len(number)
                    end_of_number = position

                    if row_num == 0:
                        # deal with situation where start_of_number and end_of_number are at the edge (so +1 and -1 causes an error)
                        neighbours = matrix[row_num+1][start_of_number - 1: end_of_number + 1] + \
                                     matrix[row_num][start_of_number - 1: end_of_number + 1]
                        if any((i != '.') and (not i.isnumeric()) for i in neighbours):
                            valid_parts += int(number)
                        else:
                            pass

                        number = ''

                    elif row_num != len(matrix) - 1:
                        neighbours = matrix[row_num - 1][start_of_number - 1: end_of_number + 1] + \
                                     matrix[row_num + 1][start_of_number - 1: end_of_number + 1] + \
                                     matrix[row_num][start_of_number - 1: end_of_number + 1]

                        if any((i != '.') and (not i.isnumeric()) for i in neighbours):
                            valid_parts += int(number)
                        else:
                            pass

                        number = ''

                    elif row_num == len(matrix) - 1:
                        neighbours = matrix[row_num-1][start_of_number - 1: end_of_number + 1] + \
                                     matrix[row_num][start_of_number - 1: end_of_number + 1]
                        if any((i != '.') and (not i.isnumeric()) for i in neighbours):
                            valid_parts += int(number)
                        else:
                            pass

                        number = ''


                else:
                    pass

    return valid_parts


if __name__ == '__main__':

    with open("day_3_sample.txt") as f:
        files = f.read().splitlines()
        matrix = [file for file in files]

    valid_parts = sum_part_numbers(matrix=matrix)

    print(valid_parts)