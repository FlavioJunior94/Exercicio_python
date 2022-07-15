n=int(input('Digite um numero:'))
naturais=[]
for i in range(0,n+1):
    naturais.append(i)
print(f'11- Numeros naturais de 0 a {n} em ordem Crescente: {naturais}')
print(f'12- Numeros naturais de 0 a {n} em ordem Crescente: {sorted(naturais,reverse=True)}')