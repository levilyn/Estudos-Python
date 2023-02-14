n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))

if n1 > n2:
    print('o número {} é maior que o número {}.'.format(n1, n2))

elif n2 > n1:
    print('o número {} é maior que o número {}.' .format(n2, n1))

else:
    print('os dois números são iguais.')