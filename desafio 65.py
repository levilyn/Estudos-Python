
r = n = soma = media = cont = maior = menor = 0

while r != 'N':
    n = int(input('digite um número: '))
    r = str(input('quer continuar? (S/N) ')).upper().strip()[0]
    cont += 1
    soma += n
    if n == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

media = soma / cont
print('a soma entre os números é {} e sua média é {:.2f}' .format(soma, media))
print('o maior valor é {} e o menor é {}' .format(maior, menor))
