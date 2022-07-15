n=int(input('Numero: '))
naturais_n=[n for n in range(0,n+1)]
multiplos_11=[n for n in naturais_n if n%11==0]
multiplos_13=[n for n in naturais_n if n%13==0]
multiplos_17=[n for n in naturais_n if n%17==0]
multiplos=list(set().union(multiplos_17,multiplos_11,multiplos_13))
multiplos.sort()
print(f'Resultado: {multiplos[-1]}')

