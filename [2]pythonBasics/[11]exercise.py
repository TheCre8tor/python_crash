some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'a'];
res = some_list.count('b')
# print(res)

# I'm going to loop over some_list
# I'm going to count each iteration
# If each iteration is greater than 1
# I am going to push it into a new array

duplicates = []
for item in  some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:  # I don't really understand this part.
            duplicates.append(item)

print(duplicates) 