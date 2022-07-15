while True:
    try:
        n=int(input('numero de vezes a lançar dados:'))
        break
    except:
        print('dados invalidos, tente novamente.')
        continue
naturais=[i for i in range(0,n*10)]
while True:
    try:
        i=int(input('valor de i: '))
        j=int(input('valor de j: '))
        multiplo_i = [x for x in naturais if x % i == 0]
        multiplo_j = [x for x in naturais if x % j == 0]
        break
    except:
        print('dados invalidos, tente novamente.')
        continue

multiplos=multiplo_j+multiplo_i
multiplos=set(sorted(multiplos))
multiplos=list(multiplos)
for i in range(n):
    print(multiplos[i],end=' ')