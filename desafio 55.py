maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('digite o peso da {}º pessoa: ' .format(p)))

    if p == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('o maior peso mostrado foi {}KG' .format(maior))
print('o menor peso mostrado foi {}KG'.format(menor))
