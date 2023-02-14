n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
p = nome[0]
u = nome[len(nome)-1]
print('seu primeiro nome é: {}\nseu ultimo nome é: {}' . format(p, u))
