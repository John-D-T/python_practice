"""
Problem

you're given scratch cards

there are winning numbers, then the numbers you have

figure out how many winning numbers you have

that determines your score


Method:

Create variable total_points = 0

Loop through each row ('card')

Seperate the winning numbers and numbers you have using split('|')

Then create a hashMap/list of the winning numbers

Loop through the numbers:
    If it exists in the Hashmap, remove it from the hashmap, then add a counter

    since 3 matches is worth 4 (1*2*2), that's equal to 2^3
        add 2^n to total_points

return total points

Soln: 1131 (too low)
"""


def calculate_total_points(card_matrix):

    total_points = 0
    for row in card_matrix:
        winning_hashMap = {}

        counter = 0
        card_number, numbers = row.split(': ')[0], row.split(': ')[-1]
        existing_numbers = numbers.split(' | ')[-1].split(' ')

        winning_numbers = numbers.split('|')[0].split(' ')
        for number in winning_numbers:
            if number.isnumeric():
                winning_hashMap[number] = winning_hashMap.get(number) + 1 if winning_hashMap.get(number) else 1

        for number in existing_numbers:
            if winning_hashMap.get(number):
                winning_hashMap[number] = winning_hashMap.get(number) - 1
                counter += 1

                if winning_hashMap.get(number) <= 0:
                    del winning_hashMap[number]

        exponential_counter = 2 ** (counter - 1)

        total_points += exponential_counter

    return total_points


if __name__ == '__main__':

    with open("day_4_input.txt") as f:
        file = f.read().splitlines()

    total_points = calculate_total_points(card_matrix=file)

    print(total_points)