
n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
n3 = n1 + n2
media = n3 / 2

if media < 5.0:
    print('\033[0;31m VOCÊ FOI REPROVADO!\033[0;31m sua média total foi de {} pontos' .format(media))

elif 5 >= media < 6.9:
    print('\033[0;33m VOCÊ ESTÁ DE RECUPERAÇÃO!\033[0;33m sua média total foi de {} pontos' .format(media))

elif media >= 7:
    print('\033[0;32m VOCÊ FOI APROVADO!\033[0;32m sua média total foi de {} pontos' .format(media))
