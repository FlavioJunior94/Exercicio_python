sal_carlos=float(input('Salario carlos: '))
tax_carlos=float(input('taxa mensal Carlos %: '))
tax_joao=float(input('taxa mensal Joao %: '))
sal_joao=sal_carlos/3
pou_carlos=sal_carlos
pou_joao=sal_joao
mes=1
while pou_joao<pou_carlos:
    pou_carlos=pou_carlos+(pou_carlos*(tax_carlos/100))
    pou_joao=pou_joao+(pou_joao*(tax_joao/100))
    mes+=1
print(f'Valor final de Carlos: {pou_carlos:.2f}\nValor final de Joao: {pou_joao:.2f}'
      f'\nMeses de investimentos: {mes}(em anos: {int(mes/12)})')