numeros=[]
for i in range(1,11):
    x=int(input(f'Digite o {i}º numero: '))
    numeros.append(x)
print(f'A media dos numeros digitados é: {sum(numeros)/len(numeros)}')