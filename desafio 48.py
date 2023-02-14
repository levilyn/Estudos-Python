
cont = 0
soma = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
       cont += 1
       soma += num
    print('a soma de todos os {} valores é {}' .format(cont, soma))
    