# Decorator
# Decorators are funtions that wrap other 
# functions and enhances it or change it

def decorate(func):
    def func_wrap(*args, **kwargs): # 2. Then this
        # print(*args)
        func(*args, **kwargs) # 3. This is called last
    return func_wrap  # 1. This is called

# -- Invoking Method 1 -->
@decorate
def greet(greet, emoji= '💡', last='Bye!'):
    return f'{greet} {emoji} {last}'

print(greet('Hello, How are you?', '❤️‍🩹'))


# -- Invoking Method 2 -->

# hello = decorate(greet)
# hello('*********')


# -- Invoking Method 3 -->
# decorate(greet)('**********', '🚨')