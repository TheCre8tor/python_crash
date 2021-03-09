collectData = []

for value in enumerate(['Heavens', 'shall', 'praise', 'thee']):
    collectData.append(value)

value = dict(collectData)
# print(value)

for idx,char in enumerate(collectData):
    if idx == 1:
        print(f'The value of index 1 is: {char}')
