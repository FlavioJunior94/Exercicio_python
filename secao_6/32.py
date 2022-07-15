while True:
    try:
        n=int(input('numero de vezes a lançar dados:'))
        break
    except:
        print('dados invalidos, tente novamente.')
        continue
for i in range(n):
    while True:
        try:
            d1=int(input('Dado 1: '))
            d2=int(input('Dado 2: '))
            break
        except:
            print('dados invalidos, tente novamente.')
            continue
    if d1>d2:
        print(f'{d1} é maior que {d2}')
    elif d2>d1:
        print(f'{d2} é maior que {d1}')
    elif d1==d2:
        print(f'os numeros são iguais {d1}')