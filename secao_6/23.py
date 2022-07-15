num = int(input('Digite um numero: '))
divisores=[i for i in range(1, num//2+1) if num%i==0]
divisores.append(num)
print(f"Divisores de {num} são: {divisores}")
