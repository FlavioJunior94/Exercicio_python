numeros=[]
for i in range(1,11):
    x=int(input(f'Digite o {i}º numero: '))
    numeros.append(x)
print(f'A soma dos numeros digitados é:{sum(numeros)}')