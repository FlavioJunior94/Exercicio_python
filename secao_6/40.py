numeros=[]
x=0
while x>-1:
    x=int(input('digite um numero: '))
    numeros.append(x)
print(f'O maior numero é {max(numeros)}\nO menor numero é {min(numeros)}')