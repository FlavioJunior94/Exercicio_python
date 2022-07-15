
numeros=[]
cont=1
while cont<=10:
    x = int(input(f'Digite o {cont}º numero: '))
    if x>=0:
        numeros.append(x)
        cont+=1
print(f'A media dos numeros digitados é: {sum(numeros)/len(numeros)}')