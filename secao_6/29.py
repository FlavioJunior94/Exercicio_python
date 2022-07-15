def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
x=2
s=0
for i in range(1,6):
    s+=i/fatorial(x)
    x+=2
print(f'Valor de S: {s}')