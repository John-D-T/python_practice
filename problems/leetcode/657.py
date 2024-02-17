class Solution:
    def judgeCircle(self, moves):
        # soln 1: can count the number of occurances of each letter - see if they cancel out
        # left = moves.count('L')
        # right = moves.count('R')
        # up = moves.count('U')
        # down = moves.count('D')
        #
        # return left == right and up == down

        # soln 2: create an opposite_dictionary
        # if the list is empty at the end, it's in the same position
        final_moves = []
        opposite_dictionary = {"U": "D",
                               "D": "U",
                               "L": "R",
                               "R": "L"
                               }

        for move in moves:
            if opposite_dictionary[move] in final_moves:
                final_moves.remove(opposite_dictionary[move])
            else:
                final_moves.append(move)

        return not final_moves

