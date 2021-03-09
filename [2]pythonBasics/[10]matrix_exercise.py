# Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

pixel = 0
while pixel < len(picture):
    print(''.join(str(picture[pixel]).replace('0',' ').replace('[', '').replace(']', '').replace(',', '').replace('1', '*')))
    pixel += 1

for row in picture:
    for pixel in row:
        if pixel:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')
