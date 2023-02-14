frase = str(input('''digite uma frase aqui: ''')).lower().strip()
print('analisando sua frase...')

r = frase.count('a')
p = frase.find('a')
u = frase.rfind('a')+1

print('a letra a aparece {} vezes\nsua primeira aparição é na posição {}\ne sua última aparição é na posição {}' .format(r, p, u))
