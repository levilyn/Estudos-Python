print('*' * 30)
print('analisador de triângulos')
print('*' * 30)
r1 = float(input('primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimentos podem formar um triângulo')
else:
    print('esses seguimentos não podem formar um triângulo')
