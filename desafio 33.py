num = int(input('digite um número: '))
a = int(input('digite um segundo número: '))
b = int(input('digite um terceiro número: '))

if num < a or num < b:
    menor = num

if a < num or a < b:
    menor = a

if b < num or b < a:
    menor = b

if num > a or num > b:
    maior = num

if a > num or a > b:
    maior = a

if b > num or b > a:
    maior = b

print('o maior valor digitado foi {}' .format(maior))
print('o menor valor digitado foi {}' .format(menor))
