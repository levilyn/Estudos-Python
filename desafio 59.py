opc = 0
while opc != 5:
    n1 = int(input('primeiro valor: '))
    n2 = int(input('segundo valor: '))
    print('operações: \n'
          '[1] soma\n'
          '[2] multiplicação\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa')
    opc = int(input('qual sua opção? '))

    if opc == 1:
        soma = n1 + n2
        print('você escolheu a opção 1, a soma entre os números {} e {} é {}'.format(n1, n2, soma))

    elif opc == 2:
        multi = n1 * n2
        print('você escolheu a opção 2, a multiplicação entre os números {} e {} é {}'.format(n1, n2, multi))

    elif opc == 3:
        if n1 > n2:
            print('você escolheu a opção 3, o número {} é maior que o número {}' .format(n1, n2))
        if n2 > n1:
            print('você escolheu a opção 3, o número {} é maior que o número {}' .format(n2, n1))

    elif opc == 4:
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
        print('operações: \n'
              '[1] soma\n'
              '[2] multiplicação\n'
              '[3] maior\n'
              '[4] novos números\n'
              '[5] sair do programa')
        opc = int(input('qual sua opção? '))

    elif opc == 5:
        print('você escolheu sair do programa. finalizando...')

    else:
        print('opção invalida, tente novamente')
