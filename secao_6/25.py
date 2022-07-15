naturais_mil=[n for n in range(0,1001)]
multiplos_tres=[n for n in naturais_mil if n%3==0]
multiplos_cinco=[n for n in naturais_mil if n%5==0]
multiplos=list(set().union(multiplos_cinco,multiplos_tres))
multiplos.pop(-1)
print(f'A soma de todos os numeros naturais abaixo de 1000, multiplos de 3 ou de 5 é: {sum(multiplos)}')
