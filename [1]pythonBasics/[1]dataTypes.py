# 1. FUNDAMENTAL DATA TYPES 

# 1. Int
# 2. Float
# 3. complex
# 4. bool   - boolean
# 5. str    - string
# 6. list
# 7. tuple
# 8. set
# 9. dict   - dictionary


# 2. CLASSES DATA TYPES -> Custom Types

# 3. SPECIALIZED DATA TYPES

# SPECIAL DATA TYPE
None


# EXPLANATION

# Init and float
# number = int('10')
# print(type(number))

# print((2+4))        # Int
# print(int(4/2))     # Int

# print(type(2-4))    # Int
# print(type(2 / 4)) # 0.5 - Float

# print(2 ** 3)
# print(5 // 4)
# print((6 % 4))


# Math Functions
print(round(3.1))
print(abs(-19))  # NOTE : abs -> return the absolute value of a number
                 # It removes the - dash sign at the front of any given number.
  

# Variables Best Practice

# 1. snake_case
# 2. Start with lowercase or underscore
# 3. It is case sensitive
# 4. Don't overide keywords
# 5. underscore in python signify a private variable

iq = 190;
user_id = '#2791';
_user = 'Alexander';
userName = 'Alexander Nitiola';
names = ['a', 'b', 'c', 'd'];
numb8 = 8000;

print(numb8)

# Constant Variable
""" Whenever a variable is written
    in capital letters, it means it is
    a constant variable and it should
    never be changed. """;

PI = 908;
MY_NAME = 'Alexander';

# Assigning variables to multiple value
a,b,c = 1,2,3
print(a,b,c)
 