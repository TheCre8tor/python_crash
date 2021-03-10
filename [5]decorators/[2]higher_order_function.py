# Higher Order Function
# --> A higher order function can be one of two things
# It can eighter be a function that accept another function
# or it could be a function that return another function

def another():
    return 'I am an higher order function'


def greet(func):
    return func()


print(greet(another))


# -- -->
def greet_two():
    def greet_three():
        return 'This is HOC'

    return greet_three()


print(greet_two())
