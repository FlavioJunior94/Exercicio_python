num = int(input('Digite um numero: '))
divisores=[i for i in range(1, num//2+1) if num%i==0]

print(f"A soma dos Divisores de {num} é {sum(divisores)}")