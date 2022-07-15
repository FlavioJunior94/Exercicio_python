up=[]
down=[]
for i in range(1,100,2):
    up.append(i)
for j in range(1,51):
    down.append(j)
lista=[]
for x in range(0,51):
   lista.append(up[x]/down[x])

print(f"Resultado: {sum(lista)}")