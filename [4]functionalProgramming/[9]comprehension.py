# List, Set, and Dictionary Comprehension

my_list = []

for item in 'hello':
    my_list.append(item)

print(my_list)

# List Comprehension
my_list2 = [char for char in 'hello']
my_listed = [char for char in ['I', 'am', 'Alexander', 'the', 'great']]
my_numb = [num for num in range(1, 100)]
my_numb2 = [num * 2 for num in range(0, 100)]
my_numb_even = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list2)
print(my_listed)
# print(my_numb)
# print(my_numb2)
print(my_numb_even)