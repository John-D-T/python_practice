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



then loop through each row



Soln:
"""


def matrix_check(line, row_num, start_of_number, end_of_number, number, valid_parts, first_row=False, last_row=False):
    left_edge = max(0, start_of_number - 1)
    right_edge = min(len(line) - 1, end_of_number + 1)

    neighbours = matrix[row_num][left_edge: right_edge]

    if not first_row:
        neighbours += matrix[row_num - 1][left_edge: right_edge]

    if not last_row:
        neighbours += matrix[row_num + 1][left_edge: right_edge]

    if any((i != '.') and (not i.isnumeric()) for i in neighbours):
        valid_parts += int(number)

        print(int(number))

    number = ''

    return valid_parts, number

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
            if not character.isnumeric():
                # skip if we don't have a number yet
                # TODO - figure out how to handle 893
                if number != '':
                    start_of_number = position - len(number)
                    end_of_number = position

                    if row_num == 0:
                        valid_parts, number = matrix_check(line=line, row_num=row_num,
                                                           start_of_number=start_of_number, end_of_number=end_of_number,
                                                           number=number, valid_parts=valid_parts, first_row=True)

                    elif row_num != len(matrix) - 1:
                        valid_parts, number = matrix_check(line=line, row_num=row_num,
                                                           start_of_number=start_of_number, end_of_number=end_of_number,
                                                           number=number, valid_parts=valid_parts)

                    elif row_num == len(matrix) - 1:
                        valid_parts, number = matrix_check(line=line, row_num=row_num,
                                                           start_of_number=start_of_number, end_of_number=end_of_number,
                                                           number=number, valid_parts=valid_parts, last_row=True)

                else:
                    pass

    return valid_parts


if __name__ == '__main__':

    with open("day_3_input.txt") as f:
        files = f.read().splitlines()
        matrix = [file + '.' for file in files]

    valid_parts = sum_part_numbers(matrix=matrix)

    print(valid_parts)