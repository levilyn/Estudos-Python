num = int((input('digite um número de 0 a 9999 e descubra o que cada digito representa: ')))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('o número {} é representado como:\nunidade = {}\ndezena = {}\ncentena = {}\nmilhar = {}' .format(num, u, d, c, m))
