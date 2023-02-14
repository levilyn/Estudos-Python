nome = str(input('digite seu nome completo: ')).strip()
print('estamos analisando seu nome, aguarde...')

C = nome.upper()
c = nome.lower()
l = len(nome) - nome.count(' ')
#n = nome.find(' ')
separa = nome.split()

print('seu nome em letras MAIÚSCULAS: {}\nseu nome em letras minúsculas: {}\nseu nome tem o total de: {} letras\ne seu primeiro nome tem o total de {} letras' .format(C, c, l, n))
