n=int(input('Digite o valor de n: '))
num=[]
for i in range(1,(n)*2):
    if i%2==1:
        num.append(str(i))

print(f"Valor de N= {n}\nOs {n} primeiros numeros impares são:{'-'.join(num)}")