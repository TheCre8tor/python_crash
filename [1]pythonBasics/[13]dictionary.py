# Dictionary

dictionary = {
    'name': 'Alexander',
    'last_Name': 'Nitiola',
    'username': 'darc'
}

# print(dictionary)

my_list = [
    {
        'name': 'Alexander',
        'last_Name': 'Nitiola',
        'username': 'darc',
        'address': [1, 'Mojidi', 'Ikeja'],
        'height': 260,
        'good': True
    },
    {
        'name': 'Opeyemi',
        'last_Name': 'Anold',
        'username': 'Opna',
        'address': [1, 'ogba', 'Ikeja'],
        'height': 270,
        'good': True
    }
]

# print(my_list[0]['address'][1])

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello! How are you?',
    'age': 20
}


# the get method will return a value if the first 
# argument is found in the dictionary, else it 
# will make use of the second argument as its 
# default value
age = user.get('age', 25)
# print(age)


# ANOTHER WAY OF CREATING A DICTIONARY
new_user = dict(name = 'Segun', age = 27)
# print(new_user)


# DICTIONARY METHODS
# Search for more Dicrionary Methods // Today

# print('greet' in user)

checkKeys = user.keys()
checkValues = user.values()
checkItems = user.items()
# print(checkKeys)
# print(checkValues)
# print(checkItems)


# print('Hello! How are you?' in checkValues)

# user.clear()
userClone = user.copy() # dictionary does not support [:] slice copying
userClone.pop('age')  # pop removes item from the last end
print(userClone)

userClone.update({'availability': 'offline'})
userClone.update({'greet': 'hello!'})
print(userClone)