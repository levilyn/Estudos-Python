c = float(input('digite sua quilometragem: '))
d = c > 80
if d:
    print('você foi multado!')
    e = (c-80) * 7
    print('o valor de sua multa é de R${}' .format(e))
else:
    print('você está dentro dos limites, parabéns.')
