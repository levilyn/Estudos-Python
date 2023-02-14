
s = str(input('Digite seu sexo (M/F): ')).upper()

while s not in 'MF':
    s = str(input('Digite seu sexo (M/F): ')).upper()

print('sexo registrado')
