"""
Problem broken down

Missing an engine part

add all 'part numbers' to figure this out

'part_numbers' are '*' adjacent to EXACTLY 2 part numbers (variation on part 1)
    adjacent means next to it on a matrix (diagonals are allowed)

figure out all '*' which ARE a part
    Then multiply the adjacent numbers

ideas:

initialize variable 'valid_parts' to be 0

convert into a matrix

to avoid indexing errors, add a column of '.' LEFT and RIGHT

then loop through each row
    if it's a '*':
        check all around it. For each row (above, below, same), count the number of numbers
            (how to count: re.findall(\d+))
            if there are EXACTLY 2
                multiply them, then add it to 'valid_parts'
            else:
                pass
    if it's not a '*':
        pass

return 'valid_parts'



Soln:
"""

import re

def matrix_check(line, row_num, position, valid_parts, first_row=False, last_row=False):

    # this needs to be more sophisticated - currently cutting off the full value of the adjacent numbers
    left_edge = max(0, position - 1)
    right_edge = min(len(line) - 1, position + 1)

    neighbours = matrix[row_num][left_edge: right_edge]
    neighbours_numbers = re.findall('\d+', neighbours)

    if not first_row:
        neighbours_below = matrix[row_num - 1][left_edge: right_edge]
        neighbours_numbers += re.findall('\d+', neighbours_below)

    if not last_row:
        neighbours_above = matrix[row_num + 1][left_edge: right_edge]
        neighbours_numbers += re.findall('\d+', neighbours_above)

    # count number of unique numbers in each of these rows
    if len(neighbours_numbers) == 2:
        valid_parts += int(neighbours_numbers[0]) * int(neighbours_numbers[1])

    return valid_parts

def sum_part_numbers(matrix):
    valid_parts = 0

    # through each row
    for row_num, line in enumerate(matrix):

        # through each element in a row
        for position in range(len(line)):
            character = line[position]
            if character == '*':
                    if row_num == 0:
                        valid_parts = matrix_check(line=line, row_num=row_num,
                                                           position=position,
                                                           valid_parts=valid_parts, first_row=True)

                    elif row_num != len(matrix) - 1:
                        valid_parts = matrix_check(line=line, row_num=row_num,
                                                           position=position,
                                                           valid_parts=valid_parts)

                    else:
                        valid_parts = matrix_check(line=line, row_num=row_num,
                                                           position=position,
                                                           valid_parts=valid_parts, last_row=True)
            else:
                pass

    return valid_parts


if __name__ == '__main__':

    with open("day_3_input.txt") as f:
        files = f.read().splitlines()
        matrix = ['.' + file + '.' for file in files]

    valid_parts = sum_part_numbers(matrix=matrix)

    print(valid_parts)