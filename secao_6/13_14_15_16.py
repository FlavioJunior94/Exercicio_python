n=int(input('Digite um numero:'))
naturais=[]
for i in range(0,n+1):
    naturais.append(i)
impares=[n for n in naturais if n%2==1]
pares=[n for n in naturais if n%2==0]

print(f"""
13- Pares crescente: {sorted(pares)}
14- Pares decrescente:{sorted(pares,reverse=True)}
15- Impares crescente: {sorted(impares)}
16- Impares decrescente:{sorted(impares,reverse=True)}
""")