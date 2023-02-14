
print('\033[1;33m INDICE DE MASSA CORPORAL (IMC) \033[0m')

peso = float(input('digite seu peso em KG: '))
altura = float(input('digite sua altura: '))

IMC = peso / (altura ** 2)

print('o seu IMC é de {:.2f}' .format(IMC))

if IMC < 18.5:
    print('você está abaixo do peso, cuidado!')

elif 18.5 <= IMC < 25:
    print('você está no peso ideal, parabéns!')

elif 25 <= IMC < 30:
    print('você está com sobrepeso, cuidado!')

elif 30 <= IMC < 40:
    print('você está com OBESIDADE, cuidado!')

elif IMC >= 40:
    print('você está com OBESIDADE MÓRBIDA, cuidado!')
