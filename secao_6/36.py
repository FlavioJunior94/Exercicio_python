naturais=[i for i in range(1,101)]
quadrados_n=[i**2 for i in naturais]
soma_naturais=sum(naturais)**2
soma_quadrados_n=sum(quadrados_n)

print(f'Resultado = {soma_naturais-soma_quadrados_n}')
