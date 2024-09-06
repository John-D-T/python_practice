# def character_count(string, character):
#     hashMap = {}

#     if len(string) == 0:
#         return 0

#     for item in string:
#         if item not in hashMap:
#             hashMap[item] = 1
#         else:
#             hashMap[item] += 1


#     return hashMap[character]

#     # return string.count(character)


# input = 'character'

# number = character_count(input, 'c')

# print(number)


# string1 = 'testing words seeing if they match'
# string2 = 'testing word seeing if they match'

# def mismatch_check(string1, string2):
#     match_list = []
#     mismatch_list = []

#     for string in string1.split(' '):
#         mismatch_list.append(string)

#     for string in string2.split(' '):
#         if string in mismatch_list:
#             mismatch_list.remove(string)
#         else:
#             match_list.append(string)

#     return match_list + mismatch_list


# list_of_words = mismatch_check(string1=string1, string2=string2)

# print(list_of_words)


dictionary = {"a": 3,
              "b": 5,
              "d": 10,
              "c": 2,
              "x": 10}


def nth_value(dictionary, n):
    if n > len(dictionary):
        return 0

    sorted_dictionary = sorted(dictionary.items(), key=lambda d: (d[1], d[0]), reverse=True)

    print(sorted_dictionary)
    return sorted_dictionary[n][0]


n_value = nth_value(dictionary=dictionary, n=4)

print(n_value)

# list_of_parameters = [1,2,3,10,2]

# def comparison(list_of_parameters, amount):
#     sorted_list = sorted(list_of_parameters)
#     total_amount = 0
#     counter = 0

#     while total_amount < amount:
#         value = sorted_list.pop(0)
#         if (total_amount + value) > amount:
#             return counter
#         else:
#             total_amount += value
#             counter += 1

#     return counter


# number_of_values = comparison(list_of_parameters=list_of_parameters, amount=12)

# print(number_of_values)

pre_string = "I am back."


def function(pre_string):
    hashMap = {}

    modified_string = ''

    for char in pre_string:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1

    for key, value in hashMap.items():
        modified_string += f'{key}{value}'

    return modified_string


res = function(pre_string=pre_string)

print(res)