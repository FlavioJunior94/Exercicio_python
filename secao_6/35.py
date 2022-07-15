def error():
    return print('Intervalo de valores invalido')

while True:
    try:
        valor_inicial=int(input('Digite o valor inicial: '))
        valor_final = int(input('Digite o valor final: '))
        break
    except:
        error()
        continue
if valor_inicial>valor_final:
    error()
else:
    impares=[]
    if valor_inicial%2==1:
        for i in range(valor_inicial,valor_final+1,2):
            impares.append(i)
    else:
        for i in range(valor_inicial+1,valor_final+1,2):
            impares.append(i)
    print(f'A soma dos numeros impares contidos entra {valor_inicial} e {valor_final} é de {sum(impares)}.')