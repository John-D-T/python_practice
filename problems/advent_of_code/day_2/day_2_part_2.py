"""
Problem broken down

SIMILAR TO PART 1

cubes in a bag

can be red, green, or blue

Breakdown:

    Create a dictionary with the max values for each colour.

    Initialize variable 'valid_total'. Set to 0 initially.

    Loop through each game (a row)
        set up a 0 for green, blue and red. We'll figure out the max over time

        Contains different rounds (split by semi-colon)

        Loop through each round:
            note the max value for each colour - append to dict

        At the end of the game, calculate the prodct of the max value of each colour. Add this to 'valid_total'

Note: this would be g x r time complexity (number of games x number of rounds)

Soln: 66363
"""

def determine_plausible_games(games):

    valid_total = 0

    for game in games:
        game = game.split(': ')[-1]
        max_dict = {
            "blue": 0,
            "red": 0,
            "green": 0
        }
        rounds = game.split('; ')
        for round in rounds:
            list = round.split(', ')
            for colours in list:
                colour = colours.split(' ')[1]
                count = colours.split(' ')[0]

                max_dict[colour] = max(int(count), max_dict[colour])

        power = 1
        for colour in max_dict.keys():
            power = power * max_dict[colour]

        valid_total += power

    return valid_total


if __name__ == "__main__":

    with open('day_2_input.txt') as f:
        lines = f.read().splitlines()

    valid_total = determine_plausible_games(games=lines)

    print(valid_total)



