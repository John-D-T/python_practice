class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # create a stack for numbers

        # loop through the tokens:
        # if we get a number, add it to the stack

        # if not, check if it's one of the valid operators
        # if so:
        # if there is only one element in the stack, don't do anything
        # if it's a division
        # we don't have to catch a divide by 0
        # 'truncate toward zero' = % operator

        number_stack = []

        valid_operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in valid_operators:
                if len(number_stack) < 2:
                    pass

                else:
                    second_element = number_stack.pop()
                    first_element = number_stack.pop()

                    if token == '/':
                        # print('float first ele: %s' % float(first_element))
                        # print('second_ele: %s' % second_element)
                        # print('division_res: %s' % (float(first_element) / second_element))
                        result = int(float(first_element) / second_element)
                    elif token == '+':
                        result = first_element + second_element
                    elif token == '*':
                        result = first_element * second_element
                    elif token == '-':
                        result = first_element - second_element

                    number_stack.append(result)
            else:
                number_stack.append(float(token))

        return int(number_stack.pop())


