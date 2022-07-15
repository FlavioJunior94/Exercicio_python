ano=1995
sal_funcionario=2000
aumento=0.015
sal_funcionario=sal_funcionario+(sal_funcionario*aumento)
ano=1996
while ano<=2022:
    aumento=aumento*2
    sal_funcionario=sal_funcionario+(sal_funcionario*aumento)
    ano+=1
print(f'Salario em 2022 é de {sal_funcionario:.2f}')