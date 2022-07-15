numeros=[]
for i in range(1,11):
    x=int(input(f'Digite o {i}º numero: '))
    numeros.append(x)
print(f'O menor numero é: {min(numeros)}\nO maior numero é:{max(numeros)}')