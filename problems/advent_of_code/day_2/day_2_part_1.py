"""
Problem broken down

cubes in a bag

can be red, green, or blue

Breakdown:

    Create a dictionary with the max values for each colour.

    Initialize variable 'valid_total'. Set to 0 initially.

    Loop through each game (a row)
        set up a 0 for green, blue and red. We'll figure out the max over time

        Contains different rounds (split by semi-colon)

        Loop through each round:
            if none of the values exceed the max (for any colour) for ALL rounds
            THEN the game is valid
                If so, add game id (as integer) to 'valid_total'

Note: this would be g x r time complexity (number of games x number of rounds)

Improvement: Could instead iterate through the round, obtain the max, then compare to the max values

Soln: 2369
"""

def determine_plausible_games(max_cubes, games):

    valid_total = 0

    for game in games:
        id = game.split(': ')[0].split(' ')[-1]
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

        implausible = False

        for colour in max_dict.keys():
            if max_dict[colour] > max_cubes[colour]:
                implausible = True

        if not implausible:
            valid_total += int(id)


    return valid_total





if __name__ == "__main__":

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    with open('day_2_input.txt') as f:
        lines = f.read().splitlines()

    valid_total = determine_plausible_games(max_cubes=max_cubes, games=lines)

    print(valid_total)



