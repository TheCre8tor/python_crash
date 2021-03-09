stringValue = 'Hello are you there?' 
# print(stringValue)

# This is a multi-line string
long_string = """ 
WOW
O O
--- 
"""
# print(long_string)


# --- TYPE CONVERSION ---
a = str(100)
b = int(a)
c = type(b)

# print(c)


# --- ESCAPE SEQUENCE ---
weather = 'It\'s Sunny'
# print(weather)

weather_day = "\t It\'s \"kind of \" sunny \n \t hope you have a good day!"
# print(weather_day)


# --- FORMATTED STRINGS ---
name = 'Johnny'
age = 55

# Formattted strings do start with "f"
print(f'hi {name}. You are {age} years old')  # This works on python 3

# This works on python >= 2
formatted = 'hi {}. You are {} years old'.format(name, age)
# print(formatted)

formatted = 'hi {1}. You are {0} years old'.format(name, age)
# print(formatted)

formatted = 'hi {new_name}. You are {age} years old'.format(new_name = 'sally', age = 100)
# print(formatted)


# --- STRING INDEXES / SLICING ---
# Strings are immutable
# LETTER = [0,1,2,3,4,5,6,7,8]  #List/Array
# LETTERS = '012345678'
# # [start:stop]
# print(LETTERS[0:3]) 
# # [start:stop:stepover]
# print(LETTERS[0:8:2]) 
# # [start:]
# print(LETTERS[1:])
# # [:stop]
# print(LETTERS[:5])
# # [:stepover]
# print(LETTERS[::2])
# # Reversing the string with [:stepover]
# print(LETTERS[::-1])
# print(LETTERS[::-2])


# --- STRING METHODS ---
# Python String Methods https://www.w3schools.com/python/python_ref_string.asp
# NOTE: A method start with .method() // builtin funtion is like len()
quote = 'to Be Or to be'
print(quote)
print(quote.upper())
print(quote.capitalize())
print(quote.lower().find('be'))
print(quote.find('Be'))
print(quote.lower().replace('be', 'me'))
print(quote) # String are immutable

alpha = 'cumming'
pin = alpha.upper()
print(pin)
