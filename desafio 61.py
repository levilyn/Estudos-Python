print('10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITMÉTICA (P.A)')

n1 = int(input('primeiro termo: '))
razao = int(input('razão: '))
termo = n1
cont = 1
while cont <= 10:
    print('{}' .format(termo), end=' ')
    termo += razao
    cont += 1
