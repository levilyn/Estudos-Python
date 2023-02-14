d = int(input('por quantos dias o carro foi alugado? '))
k = float(input("quantos quilometros foram rodados? "))
x = d * 60
y = k * 0.15
z = x + y
print('você utilizou o carro por {} dias e rodou {}km, então no total você pagará o total de R${}'.format(d, k, z))