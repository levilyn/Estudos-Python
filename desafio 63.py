print('SEQUÊNCIA DE FIBONACCI')

num = int(input('quantos termos deseja encontrar? '))
cont = 3
primeiro = 0
ultimo = 1

print('{} → {}'.format(primeiro, ultimo), end='')

while cont <= num:
    soma = primeiro + ultimo
    print(' → {}'.format(soma), end='')
    primeiro = ultimo
    ultimo = soma
    cont += 1
