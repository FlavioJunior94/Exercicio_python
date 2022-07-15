resultado=[]
for numero in range (1000,10000):
    alto=int(numero/100)
    baixo=int(numero%100)
    soma=alto+baixo
    quadrado_da_soma=soma**2
    if numero==quadrado_da_soma:
        resultado.append(numero)
print(f'Os numeros que Possui as propriedades propostas pelo exercicio são{resultado}')


