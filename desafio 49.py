print('TABUADA')

num = int(input('digite um valor: '))
for tab in range(0, 10):
    multiplicador = tab + 1
    resultado = num * multiplicador
    print('{} x {} = {}' .format(num, multiplicador, resultado))
