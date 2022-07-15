numero=int(input('Numero: '))
fibonnaci=[0,1]
ultimo=1
penultimo=0

if (numero==1) or (numero==2):
    print("1")
else:
    for count in range(2,numero):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        fibonnaci.append(termo)
    imp_fibo=[]
    for item in fibonnaci:
        if item<numero:
            imp_fibo.append(item)
    tamanho=len(imp_fibo)+1
    print(fibonnaci[0:tamanho])