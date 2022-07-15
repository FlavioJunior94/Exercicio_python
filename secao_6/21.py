import math
numeros=[]
for i in range(0,2):
    n=int(input('Digite um numero:'))
    numeros.append(n)
maior=max(numeros)
menor=min(numeros)
pares=[]
impares=[]
lista=[]
for i in range(menor,maior+1):
    lista.append(i)

for n in lista:
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Pares: {pares}\nImpares: {impares}')
print(f'A soma dos numeros pares: {sum(pares)}A multiplicação dos Impares {math.prod(impares)}')