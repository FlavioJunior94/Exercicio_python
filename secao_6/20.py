print('ATENÇÃO! O PROGRAMA SÓ PARA QUANDO O VALOR 1000 FOR DIGITADO.')
numeros=[]
x=0
while x!=1000:
    x=int(input('Digite um numero: '))
    numeros.append(x)
pares=[n for n in numeros if n%2==0]
print(f'Numero de valores lidos= {len(numeros)}\nNumero de Valores pares= {len(pares)}')