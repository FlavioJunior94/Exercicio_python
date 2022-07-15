from random import randrange
numero_sorteado= randrange(1,1001)
tentativas=1
while True:
    try:
        numero_escolhido=int(input('Digite um numero entre 1 e 1000, e tenta acertar o numero sorteado:'))
        if numero_escolhido >= 0 and numero_escolhido <= 1000:
            if numero_escolhido > numero_sorteado:
                print('Menor...')
                tentativas+=1
                continue
            elif numero_escolhido < numero_sorteado:
                print('Maior...')
                tentativas += 1
                continue
            elif numero_escolhido == numero_sorteado:
                print(f'Meus parabens! VOCE ACERTOU!!\n numero sorteado= {numero_sorteado}\n')
                print(f'Numero de tentativas até acertar: {tentativas}')
                break
        else:
            print('Numero não pertence ao intervalo solicitado, tente novamente')
            continue
    except:
        print('Dado invalido! ')