# *args **kwargs

# *arge -> returns a tuple
# **kwargs -> returns a dictionary

# Rules for setting parameters: params, *args, default params, **kwargs 

def super_func(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total = total + item
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=15, num2=30))