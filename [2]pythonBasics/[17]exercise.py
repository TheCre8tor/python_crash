# Exercise: Return the highest even number in a list

def highest_even(num_list):
    evens = []
    for item in num_list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

even_num = highest_even([10,2,3,4,8,11,12])
print(even_num)

# Check for an even numbers
# Check the highest of the numbers