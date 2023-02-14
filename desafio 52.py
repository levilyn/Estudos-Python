
print('IDENTIFICADOR DE NÚMEROS PRIMOS')

num = int(input('digite um valor: '))
tot = 0

for pr in range(1, num + 1):
    if num % pr == 0:
        tot += 1
        print('\033[1;32m', end=" ")
    else:
        print('\033[0m', end=" ")
    print('{}' .format(pr), end= ' ')
print('\n\033[0mo número {} foi dividido {} vezes' .format(num, tot))
if tot == 2:
    print('E POR ISSO É UM NÚMERO PRIMO')
else:
    print('E POR ISSO NÃO É UM NÚMERO PRIMO')
