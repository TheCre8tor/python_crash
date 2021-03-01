# --- Exercise 1 ---

# getValue = input('What\'s your name?')
# response = (f'My name is {getValue} and I\'m great!')
# print(response)

# birth_year = input('What year were you born?')
# birth_month = input('What month were you born?')
# res = (f'I was born on {birth_month} {birth_year}')
# print(res)

# birth_year = input('What year were you born?')
# age = 2021 - int(birth_year)
# print(f'Your age is: {age}') 


# --- Exercise 2 ---
username = input('Username')
password = input('Password')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password {hidden_password} is {password_length} letters long')