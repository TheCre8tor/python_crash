value = ['I', 'am', 'greatful']

# for item in value:
#     print(item)
    

# -- USE CASE 1 -->
idx = 0
while idx < len(value):
    # print(value[idx])
    idx = idx + 1  # You have to create this increment else the program will run forever.
# else:
#     print('I\'m done printing')

# -- USE CASE 2 -->
chat = []
while True:
    response = input('Say something: ')
    chat.append(response)
    if response == 'bye':
        break
print(' '.join(chat))