quantidade=int(input('Quantidade de numeros a ser lido: '))
numeros=[]
for i in range(1,quantidade+1):
    numeros.append(int(input(f'Digite o {i}º numero: ')))
maior=max(numeros)
x=0
for n in numeros:
    if n==maior:
        x+=1
print(f'Maior numero lido: {maior}, ele foi lido {x} vezes.')
