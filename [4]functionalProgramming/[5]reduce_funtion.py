from functools import reduce

bills = [200, 500, -150, -600, 1000]

def accumulator(prev_value, current_value):
    return prev_value + current_value

print(reduce(accumulator, bills, 0))

