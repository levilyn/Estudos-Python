
cont = num = soma = 0

num = int(input('Digite um número (digite 999 se quiser parar de rodar): '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (digite 999 se quiser parar de rodar): '))

print('ok, você digitou {} números e a soma entre eles é {}' .format(cont, soma))
