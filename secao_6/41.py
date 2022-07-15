r='vazio'
while r!=0:
    r1=int(input('Vaor de R1: '))
    r2=int(input('Vaor de R2: '))
    try:
        r=(r1*r2)/(r1+r2)
    except ZeroDivisionError:
        print('\nERRO, DIVISÃO POR ZERO! \n')
    except:
        print('erro,tente novamente')
    print(f'Resultado de R: {r}')
print('\nprograma finalizado com sucesso!')