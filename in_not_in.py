"""operadores in e not in 
strings sao iteraveis
0 1 2 3 4 5 6
M a t e u s
7 6 5 4 3 2 1
"""

#name = 'Matheus'
#print(name[2])
#print(name[-4])
#print('heu' in name)
#print('vas' in name)
#print(10 * '-')
#print('heu' not in name)
#print('vas' not in name)

name = input('what your name: ')
find = input('Type what you want to find:')

if find in name:
    print(f'{find} is in {name}')
else:
    print(f'{find} is not in {name}')