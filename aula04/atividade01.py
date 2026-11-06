valor = float(input("informe o valor da compra"))

if valor > 250:
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f'Desconto de 16% aplicado! \nValor final: {valor_final:.2f} ')

else:
    print(f'Sem desconto. Valor da compra: R$ {valor:.2f} ')