"""
Problem broken down

cubes in a bag

can be red, green, or blue

Breakdown:

    Create a dictionary with the max values for each colour.

    Initialize variable 'valid_total'. Set to 0 initially.

    Loop through each game (a row)
        Contains different rounds (split by semi-colon)

        Loop through each round:
            if none of the values exceed the max (for any colour) for ALL rounds
            THEN the game is valid
                If so, add game id (as integer) to 'valid_total'

Note: this would be g x r time complexity (number of games x number of rounds)

Improvement: Could instead iterate through the round, obtain the max, then compare to the max values
"""




