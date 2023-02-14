
soma = 0
pares = 0

for n in range(1, 7):
    num = int(input('digite {} valor: ' .format(n)))
    if num % 2 == 0:
        soma += num
        pares += 1
print('você digitou {} números pares e a soma entre eles é {}' .format(pares, soma))
