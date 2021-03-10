# map, filter, zip and reduce

my_list = [1, 2, 3, 4, 5]

def mulyiply_by2(item):
    return item * 2

mult = list(map(mulyiply_by2, my_list))
print(mult)


# -- Capitalizing names in list -->

usernames = ['jerry', 'tunde', 'princess']
def username_to_cap(names):
    return f'{names[0].capitalize()}{names[1:]}'

user_res = list(map(username_to_cap, usernames))
print(user_res)

