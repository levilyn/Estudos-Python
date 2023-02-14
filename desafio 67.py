print('*' * 18)
print('    TABUADA')
print('*' * 18)

while True:
    n = int(input('digite um número: '))
    print('*' * 18)

    if n < 0:
        print('NÚMERO INVÁLIDO, O PROGRAMA ESTÁ SENDO ENCERRADO.')
        break

    for mult in range(0, 10):
        multiplicador = mult + 1
        resp = n * multiplicador
        print(f'{n} x {multiplicador} = {resp}')
    print('*' * 18)
