"""

Problem: Instead of winning points, you get MORE scratchcards
    the scratchcards you get depends on how many matches and which card you're on
    e.g. you're on card 2 and get 3 matches
            you get scratchcards: 3,4,5
(recursive?/hashmap with counter?)


then count how many scratchcards you end up with


Soln: 6283755

Time taken: 23 seconds

"""

import datetime


def calculate_total_scratchcards(card_matrix):

    total_scratchcards = 0
    reference_hashmap = {}

    for row in card_matrix:
        winning_hashMap = {}
        counter = 0

        card_number, numbers = row.split(': ')[0].split(' ')[-1], row.split(': ')[-1]

        previously_solved = reference_hashmap.get(card_number)

        if previously_solved:
            for i in reference_hashmap[card_number]:
                card_matrix.append(card_matrix[int(card_number) + i])

        else:
            our_numbers = numbers.split(' | ')[-1].split(' ')
            winning_numbers = numbers.split('|')[0].split(' ')

            for number in winning_numbers:
                if number.isnumeric():
                    winning_hashMap[number] = winning_hashMap.get(number) + 1 if winning_hashMap.get(number) else 1

            for number in our_numbers:
                if winning_hashMap.get(number):
                    winning_hashMap[number] = winning_hashMap.get(number) - 1
                    counter += 1

                    if winning_hashMap.get(number) <= 0:
                        del winning_hashMap[number]

            reference_list = [i for i in range(counter)]

            for i in reference_list:
                card_matrix.append(card_matrix[int(card_number) + i])

            reference_hashmap[card_number] = reference_list

        total_scratchcards += 1

    return total_scratchcards


if __name__ == '__main__':

    with open("day_4_input.txt") as f:
        file = f.read().splitlines()

    print(f"Start time: {datetime.datetime.now().strftime('%H:%M:%S')}")

    total_scratchcards = calculate_total_scratchcards(card_matrix=file)

    print(total_scratchcards)

    print(f"End time: {datetime.datetime.now().strftime('%H:%M:%S')}")