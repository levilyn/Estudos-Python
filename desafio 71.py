print('-$' * 20)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('-$' * 20)

valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
ced = 100
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1

    else:
        if totced > 0:
            print(f'o total de {totced} cédulas de R${ced}')

        if ced == 100:
            ced = 50

        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 5

        elif ced == 5:
            ced = 2

        totced = 0

        if total == 0:
            break
