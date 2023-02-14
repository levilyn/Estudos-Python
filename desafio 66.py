n = c = s = 0

while True:
    n = int(input('digite um número (digite 999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1

print(f'foram digitados {c} números e a soma entre eles é de {s}')
