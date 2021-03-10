# This is a pure function --> ✔️
def mulyiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list

print(mulyiply_by2([1,2,3,4,5]))


# This is not a pure function --> ❌
def mulyiply_by3(list):
    new_list = []
    for item in list:
        new_list.append(item * 3)

    # This is not a pure function anymore
    # because it interact with print which
    # is not part of the multilpy_by3 scope

    return print(new_list) # This is called a side effect

mulyiply_by3([1,2,3,4,5])


# This is not a pure function --> ❌
# It has a side effect because it interact with
# the list in the global scope.
new_list = []

def mulyiply_by4(list):
    for item in list:
        new_list.append(item * 4)
    return new_list

print(mulyiply_by4([1,2,3,4,5])) 


# NOTE: It's impossible to have only pure function in 
# our program, but wherever you can, just do it.