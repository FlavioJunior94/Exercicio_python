from statistics import mean
idade=1
idades=[]
while idade >0:
    idade=int(input('Idade: '))
    if idade>0:
        idades.append(idade)
print(f'A media das idades é {mean(idades)}')