def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n=int(input('Numero: '))
e=0
for i in range(1,n+1):
    e=e+(1/fatorial(i))
print(f'valor de E: {e}')