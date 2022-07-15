n=int(input('Numero: '))
s1=[x for x in range(1,n+1)]
s2=[x for x in range(1,(2*n)-1)]
s3=[x for x in range(1,(2*n)-1,2)]
print(f"""
sequencia 1= {s1}
sequencia 2= {s2}
sequencia 3= {s3}
""")