"""
Problem broken down

parse each string in a list

combine first and last digit to form a 2-digit number
    Now we count worded numbers as a valid number!

then add all these together

idea:
    set variable sum_calibration to 0
    loop through each string
        then place right and left pointers
            check if the value is a number
                if it is:
                    add to list
                    (don't need to do anything to 'potential_worded_number' since it's useless for that pointer now

                if not:
                    append to a variable called 'potential_worded_number'
                        for left, we append to the back. For right, we append from the front
                    check if the 'potential_worded_number' exists in our hashmap. Return the integer value this equates to
                        hash map is fine since we're dealing with single digits.
                    move the pointer

    form a digit with this, and append to sum_calibration

    note: if left = right (only one digit), then return that number twice as a 2-digit number

    return sum_calibration
"""


def generate_calibration(list_of_alphanumerics):

    sum_calibration = 0

    for line_of_text in list_of_alphanumerics:
        print('dealing with:' + line_of_text)
        lp = 0
        rp = len(line_of_text) - 1

        right_status = False
        left_status = False

        while right_status is False or left_status is False:
            if line_of_text[lp].isnumeric():
                left_status = True
            else:
                lp += 1

            if line_of_text[rp].isnumeric():
                right_status = True

            else:
                rp -= 1

        # else:
        two_digit_string = f"{line_of_text[lp]}{line_of_text[rp]}"
        value = int(two_digit_string)

        print(f"value is {value}")
        sum_calibration += value

    return sum_calibration


if __name__ == '__main__':

    # read .txt into a list
    with open('day_1_input.txt') as f:
        lines = f.readlines()

    sum_calibration = generate_calibration(list_of_alphanumerics=lines)

