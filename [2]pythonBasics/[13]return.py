# A function should do one thing really well.
# A funtion should return something.

# FUNCTION RETURNING ANOTHER FUNCTION

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1,num2)

print(sum(10,20))


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func

print(sum(0,0)(5,45))