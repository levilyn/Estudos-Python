
idadeg = idadef = sexom = sexof = 0

while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Como você se identifica (F/M)? ')).lower().strip()[0]
    opc = str(input('deseja continuar (S/N)? ')).lower().strip()[0]

    if idade > 18:
        idadeg += 1

    if sexo == 'f':
        sexof += 1
        if idade < 20:
            idadef += 1

    if sexo == 'm':
        sexom += 1

    if opc == 'n':
        break

print(f'Foram cadastrados {sexom} homens.\nForam cadastradas {sexof} mulheres.')
print(f'Há {idadef} mulheres com menos de 20 anos.')
print(f'Há {idadeg} maiores de 18 anos.')
