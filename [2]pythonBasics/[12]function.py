# FUNCTION
# -- -->
def say_hello(greet):
    print(greet)

say_hello('Hello') 
say_hello('How are you today?') 
say_hello('Are you there?') 

# Exercise!
tree = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

diamond = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0]
]

def matrix(picture):
    for row in picture:
        for pixel in row:
            if pixel:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print(' ')

matrix(tree)
matrix(diamond)


# -- PARAMETERS VS ARGUMENT -->

# Default Parameters
def greet(name="Dart Vader", emoji="😈"):
    print(f'Hello {name}{emoji}')
    return f'I\'m so proud of you; {name}😎' 

# Positional Arguments
res = greet('Alexander', '😋')
print(res)

# Keyword Arguments
res = greet(emoji='😎', name='Opeyemi')
print(res)

# Using the default parameter
greet()


# EVEN OR ODD NUMBER CHECKER

# def is_even(number):
#     if number % 2 is 0:
#         return f'{number} is an even number 🤗'
#     else:
#         return f'{number} is an odd number 😓'

def is_even(number):
    if number % 2 is 0:
        return f'{number} is an even number 🤗'
    return f'{number} is an odd number 😓'

num_type = is_even(1001)
print(num_type)