fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for i in range(len(fruits)):
    print(f'{i+1} | {fruits[i]}')
for i in enumerate(fruits):
    print(f'{i[0]+1} | {i[1]}')

for i,j in enumerate(fruits):
    print(f'{i+1} | {j}')