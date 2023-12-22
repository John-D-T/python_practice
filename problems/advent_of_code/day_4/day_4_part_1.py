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
"""