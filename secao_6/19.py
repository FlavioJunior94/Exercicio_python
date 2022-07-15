while True:
    numero=int(input('digite um valor entre 100 e 999:\n'))
    if numero>=100 and numero<=999:
        break
    else:
        print('Valor invalido, tente novamente!')
        continue

uni=numero%10
dez=(numero/10)%10
cen=(numero/100)%10
print(f'Os numeros que compoe {numero} são: {int(cen)}, {int(dez)} e {uni}')