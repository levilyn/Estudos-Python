
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    opc = int(input('digite um número de 0 a 20: '))
    if 0 <= opc <= 20:
        break
    print('número inválido. Tente novamente')
print(f'você selecionou o número {numeros[opc]}')
