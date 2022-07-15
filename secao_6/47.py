def soma(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def divi(x,y):
    return x/y
opcao=0
while opcao!=5:
    try:
        opcao = int(input(
            '\nMENU\n1=adição\n2=subtração\n3=multiplicação\n4=divisão\n5=saida\nDigite o numero correspondente a sua escolha:'))
        if opcao>=1 and opcao<=4:
            x=int(input('Digite o primeiro valor:'))
            y=int(input('Digite o segundo valor:'))

        if opcao==1:
            print(f'A soma dos valores é {soma(x, y)}\n')
        elif opcao==2:
            print(f'A diferença dos valores é {sub(x, y)}\n')
        elif opcao==3:
            print(f'O produto dos valores é {mult(x, y)}\n')
        elif opcao==4:
            print(f'A divisão dos valores é {divi(x, y)}\n')
        elif opcao==5:
            print('\nENCERRANDO O PROGRAMA\n')
            break
        else:
            print('Opção invalida!\n')
    except:
        print('Valores invalidos, tente novamente.')