print('10 primeiros termos de uma Progressão Aritmética (P.A)')

n1 = int(input('primeiro termo: '))
razao = int(input('razão: '))
termo = n1
cont = 1
c = 0
total = 0
n2 = 10

while n2 != 0:
    total += n2

    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
        c += 1
    print('PAUSA')

    n2 = int(input('quer mostrar mais quantos termos? '))
    if n2 == 0:
        print('progressão finalizada, você procurou por {} termos' .format(c))
