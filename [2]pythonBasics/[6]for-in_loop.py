# The FOR-IN LOOP
name = []
count = ['Alexander', 'goes', 'to', 'school']
for item in count:
    name.append(item)
print(name)

# NEXTED LOOP
# for item in count:
#     for x in ['a','b','c']:
#         print(item)
#         print(x)


# LOOPING THROUGH AN OBJECT
user = {
    "name": "Alexander",
    "age": 26,
    "occupation": "programming"
}

for key, value in user.items():
    print(value)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for item in range(1, 10):
    # if item is not 0:
        print(item)