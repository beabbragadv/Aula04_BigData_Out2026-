#Bônus por desempenho de vendas

salario= float(input('Informe o valor do salario: R$' ))
vendas = float(input('Total das vendas: R$'))

if vendas >= 1000:
    bonus = 150.00
    salario_final = salario + bonus

elif vendas >= 500.00:
    bonus = 75.00
    salario_final = salario + bonus

else:
    bonus = 0.00

total_com_bonus = vendas + bonus

print(f'Vendas: R$ {vendas:.2f}')
print(f'Bônus: R$ {bonus:.2f}')
print(f'Total com bônus: R$ {total_com_bonus:.2f}')
    