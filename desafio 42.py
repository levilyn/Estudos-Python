n1 = float(input('primeiro segmento: '))
n2 = float(input('segundo segmento: '))
n3 = float(input('terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('todos os lados de seu triângulo são iguais, então o seu triângulo é equilátero!')

    elif n1 != n2 != n3 != n1:
        print('todos os lados do seu triângulo são diferentes, então seu triângulo é escaleno')

    else:
        print('seu triângulo tem dois lados iguais, então seu triângulo é isósceles!')
else:
    print('esses seguimentos NÃO podem formar um triângulo')
