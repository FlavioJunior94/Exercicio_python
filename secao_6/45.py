def km_ms():
    while True:
        try:
            x=int(input('Digite o valor em Km/h: '))
            break
        except:
            print('valor invalido tente novamente!')
            continue
    return print(f'Resultado:{x / 3.6}m/s')
def ms_km():
    while True:
        try:
            x=int(input('Digite o valor em m/s: '))
            break
        except:
            print('valor invalido tente novamente!')
            continue
    return print(f'Resultado:{x * 3.6}Km/h')

while True:
    print('\nEscolha uma opção: ')
    try:
        opcao=int(input('\n1= converter de km/h para m/s\n2= converter de m/s para km/h\n3=sair\n'))
    except:
        print('dado invalido!')
        break
    if opcao==1:
        km_ms()
    elif opcao==2:
        ms_km()
    elif opcao==3:
        break
    else:
        print('Opção invalida, tente novamente!')
print('Programa finalizado!')