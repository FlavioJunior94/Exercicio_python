import math
conjunto=[]
for num in range(0,3):
    num = float(input('digite um valor: '))
    conjunto.append(num)

quadrado={conjunto[i]:float(conjunto[i]**2) for i in range(len(conjunto))}
cubo={conjunto[i]:float(conjunto[i]**3) for i in range(len(conjunto))}
raiz_conjunto={conjunto[i]:float(math.sqrt(conjunto[i])) for i in range(len(conjunto))}

print('\n Quadrado:')
for chave, item in quadrado.items():
    print(f'O quadrado de {chave} é {item}.')

print('\n Cubo:')
for chave, item in cubo.items():
    print(f'O cubo de {chave} é {item}.')

print('\n Raiz Quadrada:')
for chave, item in raiz_conjunto.items():
    print(f'A raiz quadrada de {chave} é {item}.')