"""
Problem broken down

parse each string in a list

combine first and last digit to form a 2-digit number
    Now we count worded numbers as a valid number!

then add all these together

idea:
    set variable sum_calibration to 0
    loop through each string
        DON'T use right and left pointers. Go through the string sequentially and use regex!

        create a regex list

        create a dictionary with word: number

        search the whole string for anything which matches the regex list

        then loop through the list of strings
            if they match the dictionary, return the integer value

        then find the last and first numbers
            form a digit with this, and append to sum_calibration

    return sum_calibration
"""
import re

def generate_calibration(list_of_alphanumerics):

    sum_calibration = 0

    search_pattern = re.compile(r'(?:\d|zero|one|two|three|four|five|six|seven|eight|nine)')

    number_hashMap = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    cleaning_hashMap = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for line_of_text in list_of_alphanumerics:
        for number in cleaning_hashMap:
            line_of_text = line_of_text.replace(number, cleaning_hashMap[number])

        nums = search_pattern.findall(line_of_text)

        for i in range(len(nums)):
            if nums[i] in number_hashMap.keys():
                nums[i] = number_hashMap[i]

        value = nums[0] + nums[-1]

        sum_calibration += int(value)


    return sum_calibration


if __name__ == '__main__':

    # read .txt into a list
    with open('day_1_input.txt') as f:
        lines = f.readlines()

    sum_calibration = generate_calibration(list_of_alphanumerics=lines)


