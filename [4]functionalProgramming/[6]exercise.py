from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def pet_cap(pet):
    return f'{pet[0].upper()}{pet[1:]}'

get_pet = list(map(pet_cap, my_pets))
print(get_pet)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()

sort_zip = list(zip(my_strings, my_numbers))
print(sort_zip)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_result(score):
    return score > 50

score_higher = list(filter(filter_result, scores))
print(score_higher)


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
clone_numbers = my_numbers[:]
clone_numbers.extend(scores)

def combine(prev_value, curr_value):
    return prev_value + curr_value

total_num = reduce(combine, clone_numbers, 0)
print(total_num)