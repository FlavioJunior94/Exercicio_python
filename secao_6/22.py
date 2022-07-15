print('Digite as notas: o progrma irá para ao digitar uma nota menor que 10 e maior que 20: \n')
x=10
notas=[]
while x>=10 and x<=20:
    x=int(input('Digite uma nota: '))
    notas.append(x)
notas.pop(-1)
notas_str=[str(n) for n in notas]
print(f"Notas = {' - '.join(notas_str)}")
print(f'Media de notas é:{(sum(notas)/len(notas))}')
